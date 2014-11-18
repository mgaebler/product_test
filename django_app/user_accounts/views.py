#coding: utf-8
import logging
from datetime import datetime
from hashlib import sha1

from django.core.urlresolvers import reverse
from django.core.mail import send_mail, send_mass_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.db.models import Q
from django.template import Context
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.views.generic import FormView, UpdateView, ListView
from django.shortcuts import redirect, get_object_or_404


from braces.views import LoginRequiredMixin
from simple_bank.models import create_transfer, Account, Transfer

from .models import UserAccount
from . import forms


logger = logging.getLogger(__name__)


def login_view(request):
    email = request.POST.get('user[email]', None)
    password = request.POST.get('user[password]', None)
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.add_message(request, messages.INFO, _(u'Login erfolgreich'))
            if not user.profile_complete:
                messages.add_message(request, messages.INFO, _(u'Bitte vervollständige dein Profil'))
                return redirect('user:settings')
        else:
            messages.add_message(request, messages.ERROR, _(u'Dieser Account ist nicht aktiviert.'))
            return redirect('user:login_form')
    else:
        messages.add_message(request, messages.ERROR, _(u'Falscher Benutzername oder Password'))
        return redirect('user:login_form')

    return redirect('home')


def register_verify(request, token):
    # activate user and redirect to the password form
    user = get_object_or_404(UserAccount, confirmation_token=token)
    user.confirmation_at = timezone.now()
    user.is_active = True
    user.confirmation_token = ''
    user.save()
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    return redirect(reverse('user:set_password'))


def logout_view(request):
    logout(request)
    messages.info(request, _(u'Du hast dich erfolgreich ausgeloggt.'))
    return redirect('home')


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(
        request,
        uidb64=uidb64,
        token=token,
        template_name='profiles/password/password_reset_confirm.jinja',
        # token_generator=default_token_generator,
        # set_password_form=SetPasswordForm,
        post_reset_redirect=reverse('user:password_reset_complete'),
        current_app=None, extra_context=None
    )


def reset(request):
    return password_reset(
        request,
        is_admin_site=False,
        template_name='profiles/password/password_reset_form.jinja',
        email_template_name='profiles/password/password_reset_email.jinja',
        subject_template_name='profiles/password/password_reset_subject.txt',
        password_reset_form=PasswordResetForm,
        post_reset_redirect=reverse('user:password_reset_success'),
        from_email=None,
        current_app=None,
        extra_context=None,
        html_email_template_name='profiles/password/password_reset_html_email.jinja'
    )


class PasswordChangeView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'profiles/password/password_change.jinja'


class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = 'profiles/password/password_reset.jinja'

    def get_success_url(self):
        return reverse('user:password_reset_success')


class PasswordSetView(LoginRequiredMixin, FormView):
    template_name = 'profiles/password/password_set.jinja'
    form_class = forms.PasswordSetForm

    def form_valid(self, form):
        password = form.cleaned_data['password']
        user = UserAccount.objects.get(pk=self.request.user.pk)
        user.password = make_password(password=password)
        user.save()

        return super(PasswordSetView, self).form_valid(form)

    def get_success_url(self):
        messages.info(self.request, _(u'Password wurde erfolgreich gesetzt.'))
        return reverse('user:login_form')


class UserProfileChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/settings/profile.jinja'
    model = UserAccount
    fields = (
        # 'username',
        'avatar',
        'preferred_name',
        'full_name',
        # 'email',
        # 'password',
        # 'first_name',
        # 'last_name',
        'address1',
        'address2',
        'address3',
        'postcode',
        'city',
        'country',
        # personal data
        'birth_date',
        'gender',
        'family_status',
    )

    labels = {
        'address2': '',
        'address3': '',
    }

    help_texts = {
        'avatar': _(u'Max. 10MB. Wird öffentlich angezeigt.'),
        'password': _(u'Nur, wenn Du Dein Passwort ändern willst.'),
    }

    def get_success_url(self):
        return reverse('user:settings')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = self.request.user
        if not user.profile_complete:
            user.profile_complete = True
            user.save()
            # pay the user 5 points
            create_transfer(
                sender_account=Account.objects.get(name='trendsetter'),
                receiver_account=user.bank_account.all().first(),
                amount=5,
                message=u'Vielen Dank für die Verfollständigung deines Profiles.'
            )
            messages.add_message(self.request, messages.INFO, _(u'Du hast 5 Trendpoints verdient!'))
            if user.invited_by:
                # todo: if the user has an invited_by pay the invite 5 points
                create_transfer(
                    sender_account=Account.objects.get(name='trendsetter'),
                    receiver_account=user.invited_by.bank_account.all().first(),
                    amount=5,
                    message=u'Dein Invite wurde eingelöst.'
                )

        messages.add_message(self.request, messages.INFO, _(u'Profil erfolgreich gespeichert.'))

        return super(UserProfileChangeView, self).form_valid(form)


class AccountCreateView(FormView):
    model = UserAccount
    form_class = forms.RegisterForm
    template_name = 'registration/register_form.jinja'

    def get_success_url(self):
        return reverse('user:register-success')

    def form_valid(self, form):
        invite_token = self.request.GET.get('invite', '')
        email = form.cleaned_data['email'].lower()
        token = self._generate_confirmation_token(email)

        user = UserAccount()
        user.email=email
        # user.password=None
        user.registration_at=timezone.now()
        user.confirmation_token=token
        if invite_token:
            try:
                # try to identify invite
                user.invited_by = UserAccount.objects.get(invite_token=invite_token)
            except:
                logger.exception("Invite identification failed!")
        user.save()

        self._send_verification_email(user.email, token)

        return super(AccountCreateView, self).form_valid(form)

    def _send_verification_email(self, recipient, token):
        # on success send an email with link and set a verification token
        verification_link = "{}://{}{}".format(
            self.request.scheme,
            self.request.get_host(),
            reverse('user:verify_token', kwargs={'token': token})
        )

        template = get_template('registration/registration_email.jinja')
        context = Context({'verification_link': verification_link})
        email_body = template.render(context)

        send_mail(
            subject='Confirm Mail',
            # todo: create also a text email
            message=email_body,
            from_email='registration@trendsetter.de',
            recipient_list=[recipient],
            html_message=email_body,
            fail_silently=False
        )

    @staticmethod
    def _generate_confirmation_token(email):
        time = datetime.now().isoformat()
        token = sha1(email + '\0' + time)
        return token.hexdigest()


class InviteFriendsView(FormView):
    form_class = forms.InviteFriendsForm
    template_name = 'profiles/my_site/invite_friends_form.jinja'

    def get_initial(self):
        initial = super(InviteFriendsView, self).get_initial()
        # todo: provide an invite link
        invite_link = "{}://{}{}?invite={}".format(
            self.request.scheme,
            self.request.get_host(),
            reverse('user:register'),
            self.request.user.invite_token
        )

        template = get_template('profiles/emails/invite_users_email_text.jinja')
        context = Context({
            'invite_link': invite_link,
            'user_name': self.request.user.preferred_name
        })
        email_body = template.render(context)

        initial['message'] = email_body
        initial['subject'] = _(u'Kostenlos Produkttester werden')

        self.form_class.invite_link = invite_link
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        # import pudb; pu.db

        template = get_template('profiles/emails/invite_users_email.jinja')
        context = Context({
            'email_message': data['message']
        })
        html_email_body = template.render(context)

        ## todo: send mass mail does not support html messages. We can implement that in the future, but for now we'll use send_mail
        for recipient in data['recipients']:
            send_mail(
                subject=data['subject'],
                message=data['message'],
                from_email=self.request.user.email,
                recipient_list=[recipient],
                html_message=html_email_body
            )

        # mails = ((data['subject'], data['message'], self.request.user.email, [recipient]) for recipient in data['recipients'])
        # send_mass_mail(mails, fail_silently=False)

        messages.info(self.request, _(u'Es wurde eine Einladung an deine Freude verschickt.'))
        return super(InviteFriendsView, self).form_valid(form)

    def get_success_url(self):
        return reverse('user:invite_friends')


class TransferListView(ListView):
    template_name='profiles/my_site/trendpoints.jinja'
    def get_queryset(self):
        current_user_account = self.request.user.bank_account.all().first()
        return Transfer.objects.filter(Q(sender=current_user_account)|Q(receiver=current_user_account))