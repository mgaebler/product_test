# coding=utf-8

from nose import SkipTest
from django.core.urlresolvers import reverse
from django.test import TestCase

from forms_builder.forms import fields
from forms_builder.forms.models import Form
from forms_builder.forms.models import Field
from user_accounts.models import UserAccount
from simple_bank.models import Account
from simple_bank.models import Transfer


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        pass

    def test_initial_password_screen_should_not_contain_navigation(self):
        raise SkipTest

    def test_registration_link_is_only_7_days_valid(self):
        raise SkipTest

    def test_mark_profile_as_complete_if_user_did_so(self):
        raise SkipTest


class UserInviteTestCase(TestCase):
    def setUp(self):
        pass

    def test_invite_link_is_valid(self):
        raise SkipTest


    def test_invite_user_is_set(self):
        raise SkipTest


class UserSurveysTest(TestCase):
    """Tests regarding to user my surveys.
    """
    def setUp(self):
        self.user = UserAccount.objects.create_user('test@example.com', 'secret')

        self.form = Form.objects.create(
            title="Kategorie 1",
            slug="kategorie-1",
        )

        self.field = Field.objects.create(
            label="Field 1",
            slug="field-1",
            field_type=fields.TEXTAREA,
            form=self.form,
        )

        self.form_url = reverse("user:form_detail", kwargs={"slug": self.form.slug})

    def test_anonymous(self):
        """User needs to be logged in, in order to see surveys.
        """
        response = self.client.get(self.form_url)
        self.assertEqual(response.status_code, 302)

    def test_display_of_form(self):
        self.client.login(username=self.user.email, password="secret")
        response = self.client.get(self.form_url)
        self.assertContains(response, self.form.title)
        self.assertContains(response, self.field.label)

    def test_user_fills_in_survey_completely(self):
        """Tests allocation of points after an user has filled in a survey
        completely.
        """
        self.client.login(username=self.user.email, password="secret")

        self.client.post(self.form_url, data={"field-1": "Lorem ipsum dolor 1"})
        account = Account.objects.get(customer__email=self.user.email)
        self.assertEqual(account.balance, 10)

        # There will be no points for the 2nd time.
        self.client.post(self.form_url, data={"field-1": "Lorem ipsum dolor 2"})
        account = Account.objects.get(customer__email=self.user.email)
        self.assertEqual(account.balance, 10)

        transfer = Transfer.objects.filter(receiver=account).first()
        self.assertEqual(transfer.reference, u"Umfrage 'Kategorie 1' ausgefüllt")
        self.assertEqual(transfer.amount, 10)

    def test_variable_amount_of_trendpoints(self):
        """Tests variable trendpoints.
        """
        self.form.trendpoints = 42
        self.form.save()

        self.client.login(username=self.user.email, password="secret")

        self.client.post(self.form_url, data={"field-1": "Lorem ipsum dolor 1"})
        account = Account.objects.get(customer__email=self.user.email)
        self.assertEqual(account.balance, 42)

        # There will be no points for the 2nd time.
        self.client.post(self.form_url, data={"field-1": "Lorem ipsum dolor 2"})
        account = Account.objects.get(customer__email=self.user.email)
        self.assertEqual(account.balance, 42)

        transfer = Transfer.objects.filter(receiver=account).first()
        self.assertEqual(transfer.reference, u"Umfrage 'Kategorie 1' ausgefüllt")
        self.assertEqual(transfer.amount, 42)
