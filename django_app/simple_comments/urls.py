from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^/post/(?P<page_id>\d+)/$', views.post_reply, name='new'),
)
