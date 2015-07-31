# coding: utf-8
from collections import deque
from itertools import count
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from product_test.models import ProductTest
from product_test.views import ProductTestDetail
from django.core.exceptions import PermissionDenied
from django_simple_forum.models import Forum, Topic, Post
from django_simple_forum.forms import TopicForm, PostForm
from django.views.generic import UpdateView


class ForumBaseView(ProductTestDetail):
    """Common stuff for forum views.
    """
    def get_post_paginator(self, topic_id):
        """
        Returns the post pagintor for topic with passed id.
        """
        posts_list = Post.objects.filter(topic=topic_id).order_by("created")
        return Paginator(posts_list, 10)


# forum views
class PostUpdateView(UpdateView):
    fields = ["title", "body"]
    model = Post
    success_url = "."
    template_name = 'product_test/forum/post.jinja'

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        if (not self.request.user.is_superuser) and \
           (context.get("post").creator.id != self.request.user.id):
            raise PermissionDenied
        context["slug"] = self.kwargs.get("slug")
        return context


class ForumDetailView(ForumBaseView):
    template_name = 'product_test/forum/forum.jinja'

    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)
        forum = self.get_object().forum
        context['forum'] = forum
        context['topics'] = []
        for topic in forum.topic_set.all().order_by("-created"):
            posts_paginator = self.get_post_paginator(topic.id)
            topic.last_page = posts_paginator.num_pages
            context['topics'].append(topic)

        return context


class TopicView(ForumBaseView):
    template_name = 'product_test/forum/topic.jinja'

    def get_page_range(self, current_page, total_pages, window=4):
        """
        Returns range of pages that contains current page and few pages before and after it.
        """
        # maximum length of page range is window + 1
        maxlen = window + 1
        page_range = deque(maxlen=maxlen)

        # minimum possible index is either: (current_page - window) or 1
        window_start = (current_page - window) if (current_page - window) > 0 else 1

        # maximum possible index is current_page + window or total_pages
        window_end = total_pages if (current_page + window) > total_pages else (current_page + window)

        # if we have enough pages then we should end at preferred end
        preferred_end = current_page + int(window / 2.0)

        for i in count(window_start):
            if i > window_end:
                # if we're on first page then our window will be [1] 2 3 4 5 6 7
                break
            elif i > preferred_end and len(page_range) == maxlen:
                # if we have enough pages already then stop at preferred_end
                break
            page_range.append(i)

        page_range = list(page_range)

        if page_range[0] > 1:
            page_range.insert(0, "...")

        if page_range[-1] < total_pages:
            page_range.append("...")

        return page_range

    def get_context_data(self, **kwargs):
        context = super(TopicView, self).get_context_data(**kwargs)
        topic_id = self.kwargs['topic_id']
        posts_paginator = self.get_post_paginator(topic_id)
        page = self.request.GET.get('page')
        try:
            context['posts'] = posts_paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page = 1
            context['posts'] = posts_paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            context['posts'] = posts_paginator.page(posts_paginator.num_pages)

        context["display_page_range"] = len(posts_paginator.page_range) > 1
        context["page_range"] = self.get_page_range(int(page), posts_paginator.num_pages)

        context['topic'] = Topic.objects.get(pk=topic_id)
        context['post_form'] = PostForm()

        return context


@login_required
def post_reply(request, slug, topic_id):
    form = PostForm()
    topic = Topic.objects.get(pk=topic_id)
    product_test = ProductTest.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post()
            post.topic = topic
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.creator = request.user
            post.user_ip = request.META['REMOTE_ADDR']

            post.save()

            return redirect(reverse('product_test:forum:topic-detail', kwargs={'slug': slug, 'topic_id': topic_id}))

    return render(request, 'product_test/forum/reply.jinja', {
        'form': form,
        'topic': topic,
        'product_test': product_test
    })


@login_required
def new_topic(request, slug, forum_id):
    form = TopicForm()
    forum = get_object_or_404(Forum, pk=forum_id)
    product_test = ProductTest.objects.get(slug=slug)

    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            topic = Topic()
            topic.title = form.cleaned_data['title']
            topic.description = form.cleaned_data['description']
            topic.forum = forum
            topic.creator = request.user
            topic.position = form.cleaned_data['position']
            topic.save()

            return redirect(reverse('product_test:forum:forum-detail', kwargs={'slug': slug}))

    return render(request, 'product_test/forum/new-topic.jinja', {
        'form': form,
        'forum': forum,
        'product_test': product_test
    })
