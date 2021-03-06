# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from django_simple_forum.models import Answer, Forum, Topic, Post


class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]

admin.site.register(Topic, TopicAdmin)


class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Answer, AnswerAdmin)


class AnswerAdminInline(admin.TabularInline):
    model = Answer
    extra = 0


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "topic", "creator", "created"]
    inlines = (AnswerAdminInline, )

admin.site.register(Post, PostAdmin)


class ForumTopicInline(admin.TabularInline):
    model = Topic
    extra = 0
    sortable_field_name = 'position'


class ForumAdmin(admin.ModelAdmin):
    inlines = (ForumTopicInline,)

admin.site.register(Forum, ForumAdmin)


# admin.site.register(ProfaneWord)
