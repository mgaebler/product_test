import datetime
import pytz

from django.test import TestCase
from django.core.urlresolvers import reverse

from faq.factories import FaqEntryFactory
from product_test.factories import ProductTestFactory
from product_test.models import ProductTest
from surveys.models import Survey
from surveys.models import SurveyUser
from user_accounts.models import UserAccount


class ProductListPageTestCase(TestCase):
    def setUp(self):
        self.product_test = ProductTestFactory()
        self.list_url = reverse('product_test:index')

    def test_the_title_appears_in_list_view(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, self.product_test.title)

    # product tests that are not active should not appear in the list


class ProductTestPageTestCase(TestCase):
    def setUp(self):
        self.product_test = ProductTestFactory()
        self.info_url = reverse('product_test:info', kwargs={'slug': self.product_test.slug})

    def test_the_title_appears_in_info_view(self):
        response = self.client.get(self.info_url)
        self.assertContains(response, self.product_test.title)

    def test_faq_entries_appear(self):
        faq = self.product_test.faq
        # add some entries
        entry = FaqEntryFactory.create(group=faq)
        faq_url = reverse('product_test:faq', kwargs={'slug': self.product_test.slug})
        response = self.client.get(faq_url)
        self.assertContains(response, entry.question)
        self.assertContains(response, entry.answer)


class SurveysTest(TestCase):
    def setUp(self):
        self.user = UserAccount.objects.create_user('test@example.com', 'secret')
        self.survey = Survey.objects.create(title="Title 1", url="http://www.test.de")
        self.product_test = ProductTestFactory()

    def test_display_application_survey(self):
        self.client.login(username=self.user.email, password="secret")
        result = self.client.get(reverse('product_test:info', kwargs={"slug": self.product_test.slug}))
        self.assertNotContains(result, "Bewerbung")

        self.product_test.application_survey = self.survey
        self.product_test.save()
        result = self.client.get(reverse('product_test:info', kwargs={"slug": self.product_test.slug}))
        self.assertNotContains(result, "Bewerbung")

        now = datetime.datetime.now(pytz.UTC)
        start = now - datetime.timedelta(days=-1)
        end = now - datetime.timedelta(days=1)
        
        self.product_test.application_survey_start = start
        self.product_test.application_survey_end = end
        self.product_test.save()
        result = self.client.get(reverse('product_test:info', kwargs={"slug": self.product_test.slug}))
        self.assertContains(result, "Bewerbung")

    def test_display_completion_survey(self):
        self.client.login(username=self.user.email, password="secret")
        result = self.client.get(reverse('product_test:info', kwargs={"slug": self.product_test.slug}))
        self.assertNotContains(result, "Abschlussfragebogen")

        self.product_test.completion_survey = self.survey
        self.product_test.save()
        result = self.client.get(reverse('product_test:info', kwargs={"slug": self.product_test.slug}))
        self.assertNotContains(result, "Abschlussfragebogen")

        now = datetime.datetime.now(pytz.UTC)
        start = now - datetime.timedelta(days=-1)
        end = now - datetime.timedelta(days=1)
        
        self.product_test.completion_survey_start = start
        self.product_test.completion_survey_end = end
        self.product_test.save()
        result = self.client.get(reverse('product_test:info', kwargs={"slug": self.product_test.slug}))
        self.assertNotContains(result, "Abschlussfragebogen")

        SurveyUser.objects.create(user=self.user, survey=self.survey, uid=1) 
        result = self.client.get(reverse('product_test:info', kwargs={"slug": self.product_test.slug}))
        self.assertContains(result, "Abschlussumfrage")
