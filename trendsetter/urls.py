from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # static content
    url(r'^$', TemplateView.as_view(template_name='index.jinja'), name='home'),
    url(r'^ueber-uns/$', TemplateView.as_view(template_name='ueber_uns.jinja'), name='about_us'),
    url(r'^unsere-marken/$', TemplateView.as_view(template_name='unsere_marken.jinja'), name='our_brands'),
    url(r'^wie-funktioniert-es/$', TemplateView.as_view(template_name='wie_funktioniert_es.jinja'), name='how_it_works'),
    url(r'^agb/$', TemplateView.as_view(template_name='agb.jinja'), name='agb'),
    url(r'^datenschutz/$', TemplateView.as_view(template_name='datenschutz.jinja'), name='datenschutz'),
    url(r'^faq/$', TemplateView.as_view(template_name='faq.jinja'), name='faq'),
    url(r'^impressum/$', TemplateView.as_view(template_name='impressum.jinja'), name='impressum'),
    url(r'^partner-info/$', TemplateView.as_view(template_name='partner_info.jinja'), name='partner_info'),

    url(r'me/', include('user_accounts.urls', namespace='user')),
    url(r'produkttests/', include('product_test.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += patterns(
    #     '',
    #     url(r'^__debug__/', include(debug_toolbar.urls)),
    # )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)