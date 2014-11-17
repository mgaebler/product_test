# coding: utf-8

from django.views.generic import TemplateView, DetailView
from user_accounts.forms import RegisterForm
from core.models import StaticPage

class IndexView(TemplateView):
    template_name = 'index.jinja'

    def get_context_data(self, **kwargs):
        StaticPage.objects.get(slug='/')
        return {
            "content": StaticPage.objects.get(slug='/').content,
            "register_form": RegisterForm()
        }
