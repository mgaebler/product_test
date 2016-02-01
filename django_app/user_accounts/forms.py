# coding: utf-8
from django import forms
# from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from .models import UserAccount


## Using reverse at this point causes an circular import
def get_terms_of_use_and_eligibility_requirements_link():
    return u"<a target='_blank' href='/agb'>Nutzungs- und Teilnahmebedingungen</a>"


def validate_terms_of_use(value):
    if not value:
        raise ValidationError(mark_safe(u'Bitte bestätigen Sie die {}'.format(get_terms_of_use_and_eligibility_requirements_link())))


def validate_if_user_exists(value):
    if UserAccount.objects.filter(email=value).exists():
        raise ValidationError(_(u'Ein Benutzer mit dieser Emailadresse existiert bereits. Passwort vergessen?'))


class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        # split values and remove whitespace
        return map(unicode.strip, value.split(','))

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)
        for email in value:
            validate_email(email)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=254, validators=[validate_if_user_exists])
    accept_terms_of_use = forms.BooleanField(
        required=False,
        label=mark_safe(u'Ich akzeptiere die {}'.format(get_terms_of_use_and_eligibility_requirements_link())),
        validators=[validate_terms_of_use])


class PasswordSetForm(forms.Form):
    password = password = forms.CharField(
        label=_('New password'),
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )
    re_password = password = forms.CharField(
        label=_('Password (again)'),
        widget=forms.PasswordInput(render_value=False),
        max_length=100
    )


class InviteFriendsForm(forms.Form):
    recipients = MultiEmailField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 15}), help_text=_(u'Please provide the email addresses comma separated.'))
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea, help_text=_(u'Du kannst den Text verändern, solltest aber den Link nicht entfernen.'))


