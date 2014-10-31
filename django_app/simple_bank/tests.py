import factory
from django.test import TestCase
from django.contrib.auth import get_user_model
from simple_bank.models import create_transfer


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    preferred_name = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.preferred_name)


class BankAccountTestCase(TestCase):
    def setUp(self):
        # todo: Create user and bank accounts
        self.user1 = UserFactory.create()
        self.user2 = UserFactory.create()

    def test_if_bank_account_exists(self):
        # todo: After a user account is created the user should also have equivalent a bank account.
        self.assertGreater(len(self.user1.bank_account.all()), 0)

    def test_if_amount_transfer_is_valid(self):
        # Do a transaction
        # todo: make sure that the senders debit is the receivers credit.
        account1 = self.user1.bank_account.all().first()
        account2 = self.user2.bank_account.all().first()

        transfer_amount = 10
        # user1 sends user2 ten bugs
        create_transfer(
            sender_account=account1,
            receiver_account=account2,
            amount=transfer_amount,
            message='test message'
        )

        self.assertEqual(account2.balance, transfer_amount)

    def test_if_user_accounts_can_have_negative_balance(self):
        # User accounts should not have negative balance.
        # todo: Try to spend more than your amount.
        account1 = self.user1.bank_account.all().first()
        account2 = self.user2.bank_account.all().first()

        transfer_amount = 10
        # user1 sends user2 ten bugs
        create_transfer(
            sender_account=account1,
            receiver_account=account2,
            amount=transfer_amount,
            message='test message'
        )

        self.assertGreaterEqual(account1.balance, 0)

    def test_if_house_accounts_can_have_negative_balance(self):
        # House accounts should have negative balance.
        # todo: Try to spend more than your amount.
        pass
