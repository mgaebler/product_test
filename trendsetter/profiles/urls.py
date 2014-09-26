from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import login_view, logout_view, password_change
urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='profiles/product_tests.jinja'), name='profile_index'),
    url(r'^profil$', TemplateView.as_view(template_name='profiles/settings.jinja'), name='profile_settings'),
    url(r'^tests$', TemplateView.as_view(template_name='profiles/product_tests.jinja'), name='profile_tests'),
    url(r'^trendpoints$', TemplateView.as_view(template_name='profiles/trendpoints.jinja'), name='profile_trendpoints'),
    url(r'^freunde-einladen$', TemplateView.as_view(template_name='profiles/invite_friends.jinja'), name='profile_invite_friends'),

    url(r'^register/$', login_view, name='user_register'),
    url(r'^preregister/$', login_view, name='user_preregister'),
    url(r'^login-form/$', TemplateView.as_view(template_name='profiles/login_form.jinja'), name='login_form'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^change-password/$', TemplateView.as_view(template_name='index.jinja'), name='change_password'),
)
