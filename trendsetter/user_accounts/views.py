from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView

from .forms import PasswordChangeForm, UserProfileForm, RegisterForm


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
    else:
        messages.add_message(request, messages.ERROR, u'Falscher Username oder Password')
    messages.add_message(request, messages.ERROR, u'Test')
    return redirect('home')


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, u'Du hast dich erfolgreich ausgeloggt.')
    return redirect('home')


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        pass


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

