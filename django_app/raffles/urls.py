# coding: utf-8
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<url>\/\w+)$', views.RafflesDetailView.as_view(), name='detail'),
)
