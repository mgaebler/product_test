# coding: utf-8

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class VideoLinkUploadForm(forms.Form):
    video_link = forms.URLField()
