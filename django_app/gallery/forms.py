# coding: utf-8
from django import forms


class ImageUploadForm(forms.Form):
    title = forms.CharField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField()


class VideoLinkUploadForm(forms.Form):
    video_link = forms.URLField()
