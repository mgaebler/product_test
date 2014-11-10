# coding: utf-8

from django.views.generic import TemplateView
from user_accounts.forms import RegisterForm

class IndexView(TemplateView):
    template_name = 'index.jinja'

    def get_context_data(self, **kwargs):
        return {"register_form": RegisterForm()}
