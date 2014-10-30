#coding: utf8
from datetime import datetime
from hashlib import sha1

from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.template import Context
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.views.generic import FormView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from django.core.exceptions import PermissionDenied

from braces.views import LoginRequiredMixin

from .models import UserAccount
from .forms import RegisterForm, PasswordSetForm


def login_view(request):
    username = request.POST.get('user[email]', None)
    password = request.POST.get('user[password]', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.add_message(request, messages.INFO, u'Login erfolgreich')
        else:
            messages.add_message(request, messages.ERROR, u'Dieser Account ist nicht aktiviert.')
            return redirect('user:login_form')
    else:
        messages.add_message(request, messages.ERROR, u'Falscher Benutzername oder Password')
        return redirect('user:login_form')

    return redirect('home')


def register_verify(request, token):
    # activate user and redirect to the user form
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
    messages.add_message(request, messages.INFO, u'Du hast dich erfolgreich ausgeloggt.')
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
        html_email_template_name=None
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
    form_class = PasswordSetForm

    def form_valid(self, form):
        password = form.cleaned_data['password']
        user = UserAccount.objects.get(pk=self.request.user.pk)
        user.password = make_password(password=password)
        user.save()

        return super(PasswordSetView, self).form_valid(form)

    def get_success_url(self):
        messages.info(self.request, u'Password wurde erfolgreich gesetzt.')
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
    },
    help_texts = {
        'avatar': _(u'Max. 10MB. Wird öffentlich angezeigt.'),
        'password': _(u'Nur, wenn Du Dein Passwort ändern willst.'),
    }

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, u'Profil erfolgreich gespeichert.')
        return redirect('user:settings')


class AccountCreateView(FormView):
    model = UserAccount
    form_class = RegisterForm
    template_name = 'registration/register_form.jinja'

    def get_success_url(self):
        return reverse('user:register-success')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        token = self._generate_confirmation_token(email)

        user = UserAccount.objects.create_user(
            email=email, password=None,
            registration_at=timezone.now(),
            confirmation_token=token
        )

        self._send_verification_email(user.email, token)

        return super(AccountCreateView, self).form_valid(form)

    def _send_verification_email(self, recipient, token):
        # on success send an email with link and set a verification token
        verification_link = "{}{}".format(
            self.request.META['HTTP_ORIGIN'],
            reverse('user:verify_token', kwargs={'token': token})
        )

        template = get_template('registration/registration_email.jinja')
        context = Context({'verification_link': verification_link})
        email_body = template.render(context)

        send_mail(
            'Confirm Mail',
            email_body,
            'mail@trendsetter.de', # todo: change this
            [recipient], fail_silently=False
        )

    @staticmethod
    def _generate_confirmation_token(email):
        time = datetime.now().isoformat()
        token = sha1(email + '\0' + time)
        return token.hexdigest()

