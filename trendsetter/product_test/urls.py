from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import *

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='profiles/product_tests.jinja'), name='product_test_index'),
    url(r'^info$', TemplateView.as_view(template_name='profiles/settings.jinja'), name='product_test_info'),
    url(r'^forum$', TemplateView.as_view(template_name='profiles/product_tests.jinja'), name='product_test_forum'),
    url(r'^galerie$', TemplateView.as_view(template_name='profiles/trendpoints.jinja'), name='product_test_gallery'),
    url(r'^faq$', TemplateView.as_view(template_name='profiles/invite_friends.jinja'), name='product_test_faq'),
)

