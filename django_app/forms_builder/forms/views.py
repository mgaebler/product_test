# coding=utf-8

from __future__ import unicode_literals

import json
import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils.http import urlquote
from django.views.generic.base import TemplateView
# from email_extras.utils import send_mail_template

from simple_bank.models import Account
from simple_bank.models import create_transfer

from forms_builder.forms.forms import FormForForm
from forms_builder.forms.models import Form
from forms_builder.forms.models import FormEntry
from forms_builder.forms.settings import EMAIL_FAIL_SILENTLY
from forms_builder.forms.signals import form_invalid, form_valid
from forms_builder.forms.utils import split_choices

logger = logging.getLogger(__name__)


class FormDetail(TemplateView):

    template_name = "forms/form_detail.html"

    def get_context_data(self, **kwargs):
        context = super(FormDetail, self).get_context_data(**kwargs)
        published = Form.objects.published(for_user=self.request.user)
        context["form"] = get_object_or_404(published, slug=kwargs["slug"])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        login_required = context["form"].login_required
        if login_required and not request.user.is_authenticated():
            path = urlquote(request.get_full_path())
            bits = (settings.LOGIN_URL, REDIRECT_FIELD_NAME, path)
            return redirect("%s?%s=%s" % bits)

        user = getattr(request, "user", None)
        post = getattr(request, "POST", None)
        files = getattr(request, "FILES", None)

        published = Form.objects.published(for_user=request.user)
        form = get_object_or_404(published, slug=kwargs["slug"])

        context["form"] = form
        form_args = (form, context, post or None, files or None)

        try:
            instance = FormEntry.objects.get(form=form, user=user)
        except FormEntry.DoesNotExist:
            instance = None

        context["form_for_form"] = FormForForm(*form_args, instance=instance)

        if instance:
            messages.info(request, "Du hast diese Umfrage schon einmal ausgefüllt.")

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        published = Form.objects.published(for_user=request.user)
        form = get_object_or_404(published, slug=kwargs["slug"])

        try:
            instance = FormEntry.objects.get(form=form, user=request.user)
        except FormEntry.DoesNotExist:
            instance = None

        form_for_form = FormForForm(form, RequestContext(request),
                                    request.POST or None,
                                    request.FILES or None,
                                    instance=instance)
        if not form_for_form.is_valid():
            form_invalid.send(sender=request, form=form_for_form)
        else:
            messages.info(request, u"Du hast die Umfrage '{}' ausgefüllt".format(form.title))

            if instance is None:  # user hasn't completed form before.
                try:
                    sender = Account.objects.get(name="product-test")
                except Account.DoesNotExist:
                    sender = None
                    logger.critical("product-test bank account does not exist!")

                try:
                    receiver = Account.objects.get(customer__email=request.user.email)
                except Account.DoesNotExist:
                    receiver = None

                    logger.info(
                        "Couldn't add product-test points for {} for extended user profile '{}' because there is no bank account.".format(request.user.email, form.title)
                    )

                if sender and receiver:
                    create_transfer(
                        sender_account=sender,
                        receiver_account=receiver,
                        amount=form.trendpoints,
                        message="Umfrage '{}' ausgefüllt".format(form.title),
                    )
                    messages.info(request, u"Du hast {} Trendpoints verdient!".format(form.trendpoints))

            # Attachments read must occur before model save,
            # or seek() will fail on large uploads.
            attachments = []
            for f in form_for_form.files.values():
                f.seek(0)
                attachments.append((f.name, f.read()))
            entry = form_for_form.save()

            # Add user
            entry.user = request.user
            entry.save()

            form_valid.send(sender=request, form=form_for_form, entry=entry)
            self.send_emails(request, form_for_form, form, entry, attachments)
            if not self.request.is_ajax():
                return redirect(form.redirect_url or reverse("user:surveys"))
                # TODO: Why is reverse not working?
                return redirect(form.redirect_url or
                    reverse("form_detail", kwargs={"slug": form.slug}))
        context = {"form": form, "form_for_form": form_for_form}
        return self.render_to_response(context)

    def render_to_response(self, context, **kwargs):
        if self.request.is_ajax():
            json_context = json.dumps({
                "errors": context["form_for_form"].errors,
                "form": context["form_for_form"].as_p(),
                "message": context["form"].response,
            })
            return HttpResponse(json_context, content_type="application/json")
        return super(FormDetail, self).render_to_response(context, **kwargs)

    def send_emails(self, request, form_for_form, form, entry, attachments):
        subject = form.email_subject
        if not subject:
            subject = "%s - %s" % (form.title, entry.entry_time)
        fields = []
        for (k, v) in form_for_form.fields.items():
            value = form_for_form.cleaned_data[k]
            if isinstance(value, list):
                value = ", ".join([i.strip() for i in value])
            fields.append((v.label, value))
        context = {
            "fields": fields,
            "message": form.email_message,
            "request": request,
        }
        email_from = form.email_from or settings.DEFAULT_FROM_EMAIL
        email_to = form_for_form.email_to()
        if email_to and form.send_email:
            send_mail_template(subject, "form_response", email_from,
                               email_to, context=context,
                               fail_silently=EMAIL_FAIL_SILENTLY)
        headers = None
        if email_to:
            headers = {"Reply-To": email_to}
        email_copies = split_choices(form.email_copies)
        if email_copies:
            send_mail_template(subject, "form_response_copies", email_from,
                               email_copies, context=context,
                               attachments=attachments,
                               fail_silently=EMAIL_FAIL_SILENTLY,
                               headers=headers)

form_detail = FormDetail.as_view()


def form_sent(request, slug, template="forms/form_sent.html"):
    """
    Show the response message.
    """
    published = Form.objects.published(for_user=request.user)
    context = {"form": get_object_or_404(published, slug=slug)}
    return render_to_response(template, context, RequestContext(request))


def delete_form(request, slug):
    """
    Deletes the form with the passed slug:
    """
    try:
        form_entry = FormEntry.objects.get(user=request.user, form__slug=slug)
    except:
        pass
    else:
        form_entry.fields.all().delete()
        messages.info(request, "Deine Daten der Umfrage '{}' wurden gelöscht.".format(form_entry.form.title))

    return HttpResponseRedirect(reverse("user:surveys"))
