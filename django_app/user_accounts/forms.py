# coding: utf8
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import UserAccount


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )


def validate_terms_of_use(value):
    if not value:
        raise ValidationError(u'Bitte bestätigen Sie die Nutzungsrechte')


def validate_if_user_exists(value):
    if UserAccount.objects.filter(email=value).exists():
        raise ValidationError(u'Ein Benutzer mit dieser Emailadresse existiert bereits. Passwort vergessen?')


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=254, validators=[validate_if_user_exists])
    accept_terms_of_use = forms.BooleanField(required=False, validators=[validate_terms_of_use])

