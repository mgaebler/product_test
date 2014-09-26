from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect

from .forms import PasswordChangeForm


def login_view(request):
    username = request.POST.get('user[email]', None)
    password = request.POST.get('user[password]', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.add_message(request, messages.INFO, 'Login erfolgreich')
        else:
            messages.add_message(request, messages.ERROR, 'Dieser Account ist nicht aktiviert.')
    else:
        messages.add_message(request, messages.ERROR, 'Falscher Username oder Password')
        pass
    return redirect('home')


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Du hast dich erfolgreich ausgeloggt.')
    return redirect('home')


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        pass