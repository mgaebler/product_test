from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import ProductTestDetail, ProductTestList

urlpatterns = patterns(
    '',
    url(r'^$', ProductTestList.as_view(template_name='product_test/products.jinja'), name='product_test_index'),
    url(r'^(?P<slug>[\w-]+)/info$', ProductTestDetail.as_view(template_name='product_test/info.jinja'), name='product_test_info'),
    url(r'^(?P<slug>[\w-]+)/forum$', ProductTestDetail.as_view(template_name='product_test/forum.jinja'), name='product_test_forum'),
    url(r'^(?P<slug>[\w-]+)/galerie$', ProductTestDetail.as_view(template_name='product_test/gallery.jinja'), name='product_test_gallery'),
    url(r'^(?P<slug>[\w-]+)/faq$', ProductTestDetail.as_view(template_name='product_test/faq.jinja'), name='product_test_faq'),
)

