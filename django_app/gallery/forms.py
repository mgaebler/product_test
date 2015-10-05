# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class ImageUploadForm(forms.Form):
    title = forms.CharField(label=_(u"Title"), required=False)
    description = forms.CharField(label=_(u"Description"), widget=forms.Textarea, required=False)
    image = forms.ImageField(label=_(u"Image"))


class VideoLinkUploadForm(forms.Form):
    video_link = forms.URLField()
