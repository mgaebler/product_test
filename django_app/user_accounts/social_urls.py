# coding: utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from allauth.socialaccount import views as social_account_views
from allauth.account import views as account_views

connections_view = login_required(social_account_views.ConnectionsView.as_view(template_name="socialaccount/connections.jinja"))
signup_view = social_account_views.SignupView.as_view(template_name="socialaccount/signup.jinja")
login_cancelled_view = social_account_views.LoginCancelledView.as_view(template_name="socialaccount/login_cancelled.jinja")
email_verification_sent_view = account_views.EmailVerificationSentView.as_view(template_name="registration/register_form_success.jinja")


urlpatterns = patterns(
    '',
    url(r'^social/connections/$', connections_view, name='socialaccount_connections'),
    url(r'^social/signup/$', signup_view, name='socialaccount_signup'),
    url(r"^confirm-email/$", email_verification_sent_view, name="account_email_verification_sent"),
    url(r'^social/login/cancelled/$', login_cancelled_view, name='socialaccount_login_cancelled'),
)
