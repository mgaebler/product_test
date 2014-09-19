from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html.jinja'), name='home'),
    url(r'^foo/$', TemplateView.as_view(template_name='index.html'), name='foo'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
