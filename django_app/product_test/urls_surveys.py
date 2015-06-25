# coding: utf-8
from django.conf.urls import patterns, url
from surveys import views

urlpatterns = patterns('',
    url(r'^/bewerbung$', views.ApplicationView.as_view(), name='application'),
)
