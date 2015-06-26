from uuid import uuid4
from django.http import Http404
from product_test.views import ProductTestDetail
from . models import SurveyUser


def create_unique_id():
    """
    Returns a unique id.
    """
    return uuid4()


class ApplicationView(ProductTestDetail):
    """
    Displays the application survey.
    """
    template_name = "product_test/surveys/survey.jinja"

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

        # The first time a permitted user views a survey he gets an unique id.
        if not survey:
            raise Http404()
        else:
            try:
                su = SurveyUser.objects.get(
                    user=self.request.user,
                    survey=survey,
                )
            except SurveyUser.DoesNotExist:
                raise Http404()
            else:
                if not su.uid:
                    su.uid = create_unique_id()
                    su.save()
            context["uid"] = su.uid
            context["survey"] = survey
            return context
