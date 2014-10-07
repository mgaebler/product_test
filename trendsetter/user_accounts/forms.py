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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = (
            'username',
            'avatar',
            'email',
            # 'password',
            'first_name',
            'last_name',
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