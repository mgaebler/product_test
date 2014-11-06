from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ProductTestList.as_view(template_name='product_test/products.jinja'), name='index'),
    url(r'^(?P<slug>[\w-]+)/info$', views.ProductTestDetail.as_view(template_name='product_test/info.jinja'), name='info'),
    url(r'^(?P<slug>[\w-]+)/forum$', views.ProductTestDetail.as_view(template_name='product_test/forum.jinja'), name='forum'),
    url(r'^(?P<slug>[\w-]+)/galerie$', views.ProductTestDetail.as_view(template_name='product_test/gallery.jinja'), name='gallery'),
    url(r'^(?P<slug>[\w-]+)/faq$', views.ProductTestDetail.as_view(template_name='product_test/faq.jinja'), name='faq'),
    url(r'^brands$', views.ProductBrandListView.as_view(), name='brand_list'),
    url(r'^brand/(?P<slug>[\w-]+)$', views.ProductBrandDetailView.as_view(), name='brand_detail'),
)

