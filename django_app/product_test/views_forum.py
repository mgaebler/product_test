# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
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


class ReplyView(ProductTestDetail):
    template_name = 'product_test/forum/reply.jinja'

    def get_context_data(self, **kwargs):
        context = super(ReplyView, self).get_context_data(**kwargs)

        form = PostForm()
        topic = Topic.objects.get(pk=self.kwargs['topic_id'])

        if self.request.method == 'POST':
            form = PostForm(self.request.POST)

            if form.is_valid():
                post = Post()
                post.topic = topic
                post.title = form.cleaned_data['title']
                post.body = form.cleaned_data['body']
                post.creator = self.request.user
                post.user_ip = self.request.META['REMOTE_ADDR']

                post.save()

                return redirect(reverse('product_test:forum:topic-detail', slug=self.get_object().slug, topic_id=topic.pk))

        context['form'] = form
        context['topic'] = topic

        return context

#
#
# def new_topic(request, forum_id):
#     form = TopicForm()
#     forum = get_object_or_404(Forum, pk=forum_id)
#
#     if request.method == 'POST':
#         form = TopicForm(request.POST)
#
#         if form.is_valid():
#             topic = Topic()
#             topic.title = form.cleaned_data['title']
#             topic.description = form.cleaned_data['description']
#             topic.forum = forum
#             topic.creator = request.user
#
#             topic.save()
#
#             return HttpResponseRedirect(reverse('forum-detail', args=(forum_id, )))
#
#     return render_to_response('django_simple_forum/new-topic.html', {
#         'form': form,
#         'forum': forum,
#     }, context_instance=RequestContext(request))
