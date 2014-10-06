from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import password_reset, password_reset_confirm


from .forms import UserProfileForm, RegisterForm


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


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, u'Du hast dich erfolgreich ausgeloggt.')
    return redirect('home')


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(
        request,
        uidb64=uidb64,
        token=token,
        template_name='registration/password_reset_confirm.jinja',
        # token_generator=default_token_generator,
        # set_password_form=SetPasswordForm,
        post_reset_redirect=reverse('user:password_reset_complete'),
        current_app=None, extra_context=None
    )


def reset(request):
    return password_reset(
        request,
        is_admin_site=False,
        template_name='registration/password_reset_form.jinja',
        email_template_name='registration/password_reset_email.jinja',
        subject_template_name='registration/password_reset_subject.txt',
        password_reset_form=PasswordResetForm,
        post_reset_redirect=reverse('user:password_reset_success'),
        from_email=None,
        current_app=None,
        extra_context=None,
        html_email_template_name=None
    )


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'profiles/password_change.jinja'


class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = 'profiles/password_reset.jinja'

    def get_success_url(self):
        return reverse('user:password_reset_success')


class UserProfileFormView(TemplateView):
    form_class = UserProfileForm
    template_name = 'profiles/settings/profile.jinja'

    def get_context_data(self, **kwargs):
        context = super(UserProfileFormView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.request.user)
        messages.error(self.request, u'Test')
        return context

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.INFO, u'Profil erfolgreich gespeichert.')
        else:
            messages.add_message(request, messages.INFO, u'Profil konnte nicht gespeichert werden.')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class RegistrationFormView(FormView):
    template_name = 'profiles/register_form.jinja'
    form_class = RegisterForm

    def form_valid(self, form):
        pass

