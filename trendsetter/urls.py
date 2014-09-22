from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # static content
    url(r'^$', TemplateView.as_view(template_name='index.jinja'), name='home'),
    url(r'^ueber-uns/$', TemplateView.as_view(template_name='ueber_uns.jinja'), name='ueber_uns'),
    url(r'^unsere-marken/$', TemplateView.as_view(template_name='unsere_marken.jinja'), name='unsere_marken'),
    url(r'^wie-funktioniert-es/$', TemplateView.as_view(template_name='wie_funktioniert_es.jinja'), name='wie_funktioniert_es'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
