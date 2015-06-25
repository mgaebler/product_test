from uuid import uuid4
from django.http import Http404
from product_test.views import ProductTestDetail
from surveys.models import SurveyUser


def create_unique_id():
    return uuid4()


class ApplicationView(ProductTestDetail):
    template_name = "product_test/surveys/application.jinja"

    def get_context_data(self, **kwargs):
        context = super(ApplicationView, self).get_context_data(**kwargs)
        product_test = self.get_object()
        survey = product_test.application_survey

        if not survey:
            raise Http404()
        else:
            su, created = SurveyUser.objects.get_or_create(
                user=self.request.user,
                survey=survey,
            )
            # Every user is allowed to see the application survey, hence we
            # create a UID when the first visit of the survey takes place.
            if created:
                su.uid = create_unique_id()
                su.save()
            context["uid"] = su.uid
            context["survey"] = survey
            return context
