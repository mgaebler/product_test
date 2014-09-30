from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import login_view, logout_view, password_change, RegistrationFormView, UserProfileFormView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='profiles/my_site/product_tests.jinja'), name='index'),
    url(r'^profil$', UserProfileFormView.as_view(template_name='profiles/settings/profile.jinja'), name='settings'),
    url(r'^tests$', TemplateView.as_view(template_name='profiles/my_site/product_tests.jinja'), name='tests'),
    url(r'^trendpoints$', TemplateView.as_view(template_name='profiles/my_site/trendpoints.jinja'), name='trendpoints'),
    url(r'^freunde-einladen$', TemplateView.as_view(template_name='profiles/my_site/invite_friends.jinja'), name='invite_friends'),

    url(r'^register/$', RegistrationFormView.as_view(template_name='profiles/register_form.jinja'), name='register'),
    url(r'^preregister/$', login_view, name='preregister'),
    url(r'^login-form/$', TemplateView.as_view(template_name='profiles/login_form.jinja'), name='login_form'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^change-password/$', TemplateView.as_view(template_name='index.jinja'), name='change_password'),
    url(r'^forgot-password/$', TemplateView.as_view(template_name='index.jinja'), name='forgot_password'),
)
