# coding: utf8
from django import forms
from .models import UserAccount


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


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=254)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount