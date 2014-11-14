# coding: utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from product_test.models import ProductTest
from product_test.views import ProductTestDetail
from django_simple_forum.models import Forum, Topic, Post
from django_simple_forum.forms import TopicForm, PostForm


# forum view
class ForumDetailView(ProductTestDetail):
    template_name = 'product_test/forum/forum.jinja'

    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)
        forum = self.get_object().forum
        context['forum'] = forum
        context['topics'] = forum.topic_set.all().order_by("-created")

        return context


class TopicView(ProductTestDetail):
    template_name = 'product_test/forum/topic.jinja'

    def get_context_data(self, **kwargs):
        context = super(TopicView, self).get_context_data(**kwargs)
        topic_id = self.kwargs['topic_id']
        context['posts'] = Post.objects.filter(topic=topic_id).order_by("created")
        context['topic'] = Topic.objects.get(pk=topic_id)

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

            topic.save()

            return redirect(reverse('product_test:forum:forum-detail', kwargs={'slug': slug}))

    return render(request, 'product_test/forum/new-topic.jinja', {
        'form': form,
        'forum': forum,
        'product_test': product_test
    })
