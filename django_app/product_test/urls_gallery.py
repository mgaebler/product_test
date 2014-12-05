# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from product_test import views_gallery

urlpatterns = patterns('',
    url(r'^/$', views_gallery.GalleryView.as_view(), name='index'),
    url(r'^/image/upload$', views_gallery.image_upload_view, name='image_upload'),
    url(r'^/video/upload$', views_gallery.video_upload_view, name='video_upload'),
)
