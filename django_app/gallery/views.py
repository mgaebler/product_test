# coding: utf-8
from django.shortcuts import render
from django.views.generic import FormView
from gallery import forms, models


class ImageUploadView(FormView):
    form_class = forms.ImageUploadForm
    def form_valid(self, form):
        models.GalleryImage.objects.create()
        return super(ImageUploadView, self).form_valid(form)


class VideoUplaodView(FormView):
    from_class = forms.VideoLinkUploadForm
