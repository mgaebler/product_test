# coding: utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
import surveys.views

urlpatterns = patterns('',
    url(r'^/bewerbung$', surveys.views.ApplicationView.as_view(), name='application'),
    url(r'^/abschluss$', login_required(surveys.views.CompletionView.as_view()), name='completion'),
    url(r'^/login-form$', surveys.views.LoginView.as_view(), name='login_form'),
)
