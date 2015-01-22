from django.conf.urls import patterns

urlpatterns = patterns('static_pages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
