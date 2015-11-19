from django.conf.urls import patterns, url
from . import views_forum

urlpatterns = patterns('',
    url(r'^/$', views_forum.ForumDetailView.as_view(), name='forum-detail'),
    url(r'^/topic/(?P<topic_id>\d+)/$', views_forum.TopicView.as_view(), name='topic-detail'),
    url(r'^/reply/(?P<topic_id>\d+)/$', views_forum.post_reply, name='reply'),
    url(r'^/edit/(?P<pk>\d+)/$', views_forum.PostUpdateView.as_view(), name='update'),
    url(r'^/newtopic/(?P<forum_id>\d+)/$', views_forum.new_topic, name='new-topic'),
    url(r'^/answer/(?P<post_id>\d+)/$', views_forum.answer, name='answer'),
    url(r'^/edit-answer/(?P<pk>\d+)/$', views_forum.AnswerUpdateView.as_view(), name='edit-answer'),
)
