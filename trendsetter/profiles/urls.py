from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import *

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='profiles/product_tests.jinja'), name='profile_index'),
    url(r'^profil$', TemplateView.as_view(template_name='profiles/settings.jinja'), name='profile_settings'),
    url(r'^tests$', TemplateView.as_view(template_name='profiles/product_tests.jinja'), name='profile_tests'),
    url(r'^trendpoints$', TemplateView.as_view(template_name='profiles/trendpoints.jinja'), name='profile_trendpoints'),
    url(r'^freunde-einladen$', TemplateView.as_view(template_name='profiles/invite_friends.jinja'), name='profile_invite_friends'),
)
