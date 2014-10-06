from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='profiles/my_site/product_tests.jinja'), name='index'),
    url(r'^profil$', views.UserProfileFormView.as_view(), name='settings'),
    url(r'^tests$', TemplateView.as_view(template_name='profiles/my_site/product_tests.jinja'), name='tests'),
    url(r'^trendpoints$', TemplateView.as_view(template_name='profiles/my_site/trendpoints.jinja'), name='trendpoints'),
    url(r'^freunde-einladen$', TemplateView.as_view(template_name='profiles/my_site/invite_friends.jinja'), name='invite_friends'),

    url(r'^register$', views.RegistrationFormView.as_view(), name='register'),
    url(r'^preregister$', views.login_view, name='preregister'),
    url(r'^login-form$', TemplateView.as_view(template_name='profiles/login_form.jinja'), name='login_form'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^change-password$', views.PasswordChangeView.as_view(), name='change_password'),
    url(r'^reset-password$', views.reset, name='password_reset'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.reset_confirm, name='reset_confirm'),
    url(r'^reset-password-complete$', TemplateView.as_view(template_name='registration/password_reset_complete.jinja'), name='password_reset_complete'),
    url(r'^reset-password-success$', TemplateView.as_view(template_name='registration/password_reset_success.jinja'), name='password_reset_success'),
)
