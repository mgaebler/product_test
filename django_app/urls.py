from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.views.generic import TemplateView
from filebrowser.sites import site
from core.views_utils import streaming_csv_view, get_gender_birth_date_csv, all_users_csv_view

from core.views import IndexView

urlpatterns = patterns('',
    # static content
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^ueber-uns/$', TemplateView.as_view(template_name='static/ueber_uns.jinja'), name='about_us'),
    url(r'^unsere-marken/$', TemplateView.as_view(template_name='static/unsere_marken.jinja'), name='our_brands'),
    url(r'^wie-funktioniert-es/$', TemplateView.as_view(template_name='static/wie_funktioniert_es.jinja'), name='how_it_works'),

    url(r'my/', include('user_accounts.urls', namespace='user')),
    url(r'produkttests/', include('product_test.urls', namespace='product_test')),

    url(r'forum/', include('django_simple_forum.urls')),
    url(r'', include('simple_comments.urls', namespace='comments')),
    url(r'formulare', include('forms_builder.forms.urls')),

    url(r'^export/csv/all-users', all_users_csv_view),
    url(r'^export/csv/confirmed-users', streaming_csv_view),
    url(r'^export/csv/get_gender_birth_date', get_gender_birth_date_csv),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'gewinnspiele', include('raffles.urls', namespace='raffles')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('static_pages.urls')),
)

if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += patterns(
    #     '',
    #     url(r'^__debug__/', include(debug_toolbar.urls)),
    # )
    urlpatterns.insert(0, *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
