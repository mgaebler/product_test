from django.conf.urls import patterns, url
from . import views_forum

urlpatterns = patterns('',
    url(r'^/$', views_forum.ForumDetailView.as_view(), name='forum-detail'),
    url(r'^/topic/(?P<topic_id>\d+)/$', views_forum.TopicView.as_view(), name='topic-detail'),
    url(r'^/reply/(?P<topic_id>\d+)/$', views_forum.post_reply, name='reply'),
    url(r'^/newtopic/(?P<forum_id>\d+)/$', views_forum.new_topic, name='new-topic'),
)
