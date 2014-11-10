# coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='product_test/faq.jinja'), name='faq'),
)
