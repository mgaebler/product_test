from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.views import generic
from raffles.models import Raffle
from simple_comments.forms import PostForm
from static_pages.views import mk_paginator


class RafflesDetailView(generic.DetailView):
    slug_url_kwarg = "url"
    slug_field = "url"
    model = Raffle
    template_name = 'raffles/detail.jinja'

    def get_context_data(self, **kwargs):
        data = super(RafflesDetailView, self).get_context_data(**kwargs)
        data["obj_type_id"] = ContentType.objects.get_for_model(self.model).id
        data["form"] = PostForm()

        # Comments
        comments_per_page = getattr(settings, 'DJANGO_SIMPLE_COMMENTS_PER_PAGE', 10)
        comments = mk_paginator(self.request, self.object.comments.all(), comments_per_page)
        data["comments"] = comments

        return data
