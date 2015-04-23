# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals
from django import forms
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta():
        model = Comment
        exclude = ('flatpage', 'creator', 'updated', 'created', 'topic', 'user_ip', "content_type", "object_id")
