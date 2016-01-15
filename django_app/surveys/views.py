from uuid import uuid4
from django.http import Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from product_test.views import ProductTestDetail
from . models import SurveyUser


def create_unique_id():
    """
    Returns a unique id.
    """
    return uuid4()


class LoginView(ProductTestDetail):
    template_name = "product_test/surveys/login_form.jinja"


class ApplicationView(ProductTestDetail):
    """
    Displays the application survey.
    """
    template_name = "product_test/surveys/survey.jinja"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(ApplicationView, self).get(request, *args, **kwargs)
        else:
            url = reverse("product_test:surveys:login_form", kwargs={"slug": self.get_object().slug})
            if request.get_full_path():
                url += "?next={}".format(request.get_full_path())
            return redirect(url)

    def get_context_data(self, **kwargs):
        context = super(ApplicationView, self).get_context_data(**kwargs)
        product_test = self.get_object()
        survey = product_test.application_survey

        # Every user is allowed to see the application survey, hence every
        # user gets a unique ID when he views the survey the first time.
        if not survey:
            raise Http404()
        else:
            su, created = SurveyUser.objects.get_or_create(
                user=self.request.user,
                survey=survey,
            )
            if created:
                su.uid = create_unique_id()
                su.save()
            context["uid"] = su.uid
            context["survey"] = survey
            return context


class CompletionView(ProductTestDetail):
    """
    Displays the completion survey.
    """
    template_name = "product_test/surveys/survey.jinja"

    def get_context_data(self, **kwargs):
        context = super(CompletionView, self).get_context_data(**kwargs)
        product_test = self.get_object()
        survey = product_test.completion_survey

        if not survey:
            raise Http404()
        else:
            # Only users which are participate on the product test are allowed
            # to do the completion survey.
            if not product_test.takes_part_in(self.request.user):
                raise Http404()
            else:
                # The first time a permitted user views the survey he gets an
                # unique id.
                su, created = SurveyUser.objects.get_or_create(
                    user=self.request.user,
                    survey=survey,
                )
                if created:
                    su.uid = create_unique_id()
                    su.save()
                context["uid"] = su.uid
                context["survey"] = survey
                return context
