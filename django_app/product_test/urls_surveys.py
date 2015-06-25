# coding: utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from surveys import views

urlpatterns = patterns('',
    url(r'^/bewerbung$', login_required(views.ApplicationView.as_view()), name='application'),
)
