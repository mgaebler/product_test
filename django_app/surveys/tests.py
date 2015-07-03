from django.test import TestCase
from . models import Survey


class SurveysTest(TestCase):
    def setUp(self):
        self.user = UserAccount.objects.create_user('test@example.com', 'secret')

    def test_takes_part_in(self):
        Survey.objects.create()
