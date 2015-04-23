# coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from simple_shop.views import ShopItemsListView, shop_buy_item_view
from . import views

urlpatterns = patterns(
    '',
    url(r'^site$', TemplateView.as_view(template_name='profiles/my_site/product_tests.jinja'), name='index'),
    url(r'^profil$', views.UserProfileChangeView.as_view(), name='settings'),
    url(r'^tests$', TemplateView.as_view(template_name='profiles/my_site/product_tests.jinja'), name='tests'),
    url(r'^trendpoints$', views.TransferListView.as_view(), name='trendpoints'),
    url(r'^trendshop/buy/(?P<pk>\d+)/$', shop_buy_item_view, name='trendshop_buy_item'),
    url(r'^trendshop$', ShopItemsListView.as_view(template_name='profiles/my_site/trendshop.jinja'), name='trendshop'),

    url(r'^freunde-einladen$', views.InviteFriendsView.as_view(), name='invite_friends'),

    url(r'^erweitertes-profil$', views.ExtendedProfileView.as_view(), name='extended_profile'),

    url(r'^register$', views.AccountCreateView.as_view(), name='register'),
    url(r'^register-success$', TemplateView.as_view(template_name='registration/register_form_success.jinja'), name='register-success'),

    url(r'^preregister$', views.login_view, name='preregister'),

    url(r'^login-form$', TemplateView.as_view(template_name='profiles/login_form.jinja'), name='login_form'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),

    url(r'^set-password$', views.PasswordSetView.as_view(), name='set_password'),
    url(r'^change-password$', views.PasswordChangeView.as_view(), name='change_password'),
    url(r'^reset-password$', views.reset, name='password_reset'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.reset_confirm, name='reset_confirm'),
    url(r'^reset-password/complete$', TemplateView.as_view(template_name='profiles/password/password_reset_complete.jinja'), name='password_reset_complete'),
    url(r'^reset-password/success$', TemplateView.as_view(template_name='profiles/password/password_reset_success.jinja'), name='password_reset_success'),

    url(r'^verify/(?P<token>.+)$', views.register_verify, name='verify_token'),
)
