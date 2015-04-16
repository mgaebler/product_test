from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^post/(?P<obj_type_id>\d+)/(?P<obj_id>\d+)/$', views.post_reply, name='new'),
)
