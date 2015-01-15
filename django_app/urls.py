from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.views.generic import TemplateView
from filebrowser.sites import site
from core.views_utils import streaming_csv_view, get_gender_birth_date_csv

from core.views import IndexView

urlpatterns = patterns('',
    # static content
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^ueber-uns/$', TemplateView.as_view(template_name='static/ueber_uns.jinja'), name='about_us'),
    url(r'^unsere-marken/$', TemplateView.as_view(template_name='static/unsere_marken.jinja'), name='our_brands'),
    url(r'^wie-funktioniert-es/$', TemplateView.as_view(template_name='static/wie_funktioniert_es.jinja'), name='how_it_works'),
    url(r'^agb/$', TemplateView.as_view(template_name='static/agb.jinja'), name='agb'),
    url(r'^teilnahmebedingungen/$', TemplateView.as_view(template_name='static/teilnahmebedingungen.jinja'), name='eligibility_requirements'),
    url(r'^datenschutz/$', TemplateView.as_view(template_name='static/datenschutz.jinja'), name='datenschutz'),
    url(r'^faq/$', TemplateView.as_view(template_name='static/faq.jinja'), name='faq'),
    url(r'^impressum/$', TemplateView.as_view(template_name='static/impressum.jinja'), name='impressum'),
    url(r'^partner-info/$', TemplateView.as_view(template_name='static/partner_info.jinja'), name='partner_info'),

    url(r'my/', include('user_accounts.urls', namespace='user')),
    url(r'produkttests/', include('product_test.urls', namespace='product_test')),

    url(r'forum/', include('django_simple_forum.urls')),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    url(r'^export/csv/confirmed-users', streaming_csv_view),
    url(r'^export/csv/get_gender_birth_date', get_gender_birth_date_csv),
)

if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += patterns(
    #     '',
    #     url(r'^__debug__/', include(debug_toolbar.urls)),
    # )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)