# coding: utf8
from django import forms
from .models import UserAccount
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )
