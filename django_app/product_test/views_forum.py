# coding: utf-8
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from product_test.models import ProductTest
from product_test.views import ProductTestDetail
from django_simple_forum.models import Forum, Topic, Post
from django_simple_forum.forms import TopicForm, PostForm


class ForumBaseView(ProductTestDetail):
    """Common stuff for forum views.
    """
    def get_post_paginator(self, topic_id):
        """
        Returns the post pagintor for topic with passed id.
        """
        posts_list = Post.objects.filter(topic=topic_id).order_by("created")
        return Paginator(posts_list, 10)


# forum view
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

    def get_context_data(self, **kwargs):
        context = super(TopicView, self).get_context_data(**kwargs)
        topic_id = self.kwargs['topic_id']
        posts_paginator = self.get_post_paginator(topic_id)
        page = self.request.GET.get('page')
        try:
            context['posts'] = posts_paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            context['posts'] = posts_paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            context['posts'] = posts_paginator.page(posts_paginator.num_pages)
        context["display_page_range"] = len(posts_paginator.page_range) > 1
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
