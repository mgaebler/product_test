# coding: utf8
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )

