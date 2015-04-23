# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from simple_comments.models import Comment
from .forms import PostForm


@login_required
def post_reply(request, obj_type_id, obj_id):
    content_type = ContentType.objects.get(pk=obj_type_id)
    content_object = content_type.get_object_for_this_type(pk=obj_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Comment()
            post.content_object = content_object
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.creator = request.user
            post.user_ip = request.META['REMOTE_ADDR']
            post.save()

    return redirect(content_object.get_absolute_url())
