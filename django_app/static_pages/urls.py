from django.conf.urls import patterns, url

urlpatterns = patterns('static_pages.views',
    url(r'^(?P<url>.*)$', 'flatpage', name='static_page'),
)
