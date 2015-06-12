import factory
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from simple_bank.models import create_transfer, Account
from user_accounts.models import UserAccount


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    preferred_name = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.preferred_name)


class CustomerAccountTestCase(TestCase):
    def setUp(self):
        # todo: Create user and bank accounts
        self.user1 = CustomerFactory.create()
        self.user2 = CustomerFactory.create()
        self.user3 = UserAccount.objects.create_user('test@example.com', 'secret')

        self.house_account = Account.objects.create(
            name='HouseAccount',
            type='ha',
            description='A house account for the app.'
        )

    def test_if_bank_account_exists(self):
        # todo: After a user account is created the user should also have equivalent a bank account.
        self.assertGreater(len(self.user1.bank_account.all()), 0)

    def test_if_amount_transfer_is_valid(self):
        # Do a transaction
        # todo: make sure that the senders debit is the receivers credit.
        transfer_amount = 10
        account1 = self.user1.bank_account.all().first()
        account1.balance = transfer_amount
        account1.save()
        account2 = self.user2.bank_account.all().first()

        # user1 sends user2 ten bugs
        # the transfer should fail
        transfer = create_transfer(
            sender_account=account1,
            receiver_account=account2,
            amount=transfer_amount,
            message='test message'
        )

        self.assertEqual(account2.balance, transfer_amount)

    def test_user_accounts_should_not_overdraft(self):
        # User accounts should not have negative balance.
        # todo: Try to spend more than your amount.
        account1 = self.user1.bank_account.all().first()
        account2 = self.user2.bank_account.all().first()

        transfer_amount = 10
        # user1 sends user2 ten bugs
        # this is ok but should fail
        create_transfer(
            sender_account=account1,
            receiver_account=account2,
            amount=transfer_amount,
            message='test message'
        )

        # The transfer should fail and booth account amounts should be 0
        self.assertEqual(account1.balance, 0)
        self.assertEqual(account2.balance, 0)

    def test_if_house_accounts_can_make_negative_balance(self):
        # House accounts should have negative balance.
        # todo: Try to spend more than your amount.
        transfer_amount = 10
        account1 = self.house_account
        account2 = self.user2.bank_account.all().first()

        # user1 sends user2 ten bugs
        # the transfer should fail
        transfer = create_transfer(
            sender_account=account1,
            receiver_account=account2,
            amount=transfer_amount,
            message='test message'
        )

        self.assertEqual(account2.balance, transfer_amount)

    def test_debit_transfer_should_have_a_minus(self):
        account1 = self.house_account
        account2 = self.user3.bank_account.all().first()

        create_transfer(
            sender_account=account1,
            receiver_account=account2,
            amount=20,
            message='test message'
        )

        self.client.login(username="test@example.com", password="secret")

        response = self.client.get(reverse("user:trendpoints"))
        self.assertNotContains(response, "&ndash;")

        create_transfer(
            sender_account=account2,
            receiver_account=account1,
            amount=10,
            message='test message'
        )

        response = self.client.get(reverse("user:trendpoints"))
        self.assertContains(response, "&ndash;")
