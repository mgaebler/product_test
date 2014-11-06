from nose import SkipTest
from django.test import TestCase


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        pass

    def test_initial_password_screen_should_not_contain_navigation(self):
        raise SkipTest

    def test_registration_link_is_only_7_days_valid(self):
        raise SkipTest

class UserInviteTestCase(TestCase):
    def setUp(self):
        pass

    def test_invite_link_is_valid(self):
        raise SkipTest


    def test_invite_user_is_set(self):
        raise SkipTest
