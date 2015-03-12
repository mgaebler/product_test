# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from simple_comments.models import Comment
from static_pages.models import FlatPage

from .forms import PostForm


@login_required
def post_reply(request, page_id):
    flatpage = FlatPage.objects.get(id=page_id)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Comment()
            post.flatpage = flatpage
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.creator = request.user
            post.user_ip = request.META['REMOTE_ADDR']

            post.save()

    return redirect(flatpage.get_absolute_url())

    # return render(request, 'simple_comments/new_post.jinja', {
    #     'form': form,
    # })
