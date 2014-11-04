# coding: utf8
import logging

from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save


log = logging.getLogger(__name__)


class Account(models.Model):
    CURRENCY_CHOICES = (('tp', 'Trend Points'),)

    TYPE_CHOICES = (
        ('ha', 'House account'),
        ('ca', 'Customer account'),
    )

    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='ca')
    description = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bank_account', null=True, blank=True)
    balance = models.IntegerField(default=0)
    overdraft = models.IntegerField(default=0, help_text=_(u'Limit of overdraft the current account.'))
    currency = models.CharField(max_length=6, choices=CURRENCY_CHOICES, default='tp')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_possible_amount(self):
        #todo: Of cause this is a bad name for this function. Please think over and refactor.
        return self.balance + self.overdraft

    def credit(self, account):
        # give credit
        pass

    def debit(self, account):
        # make debit
        pass

    def validate_balance(self):
        # check balance based on the transfers
        pass

    def __unicode__(self):
        return u"{customer} / {name}".format(customer=self.customer, name=self.name)


class Transfer(models.Model):
    sender = models.ForeignKey(Account, related_name="sender")
    receiver = models.ForeignKey(Account, related_name="receiver")
    reference = models.CharField(max_length=255, blank=True, null=True, help_text=_(u'A short description of what why you did this.'))
    amount = models.IntegerField(default=0)
    executed = models.BooleanField(default=False)
    # todo: it could be useful also log aborted transfers
    aborted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # Don't allow transfers below the credit limit.

        if (self.sender.get_possible_amount() - self.amount) < 0 and not self.sender.type == 'ha':
            log.warning(_(u'Balance limit of {} is reached. Limit is:'.format(self.sender, self.sender.get_possible_amount())))
            return False
        elif self.sender.type == 'ha':
            log.info(_('Debit by house account'))
            super(Transfer, self).save(force_insert, force_update, using, update_fields)
        else:
            super(Transfer, self).save(force_insert, force_update, using, update_fields)

    # def clean(self):
    #     # Don't allow transfers below the credit limit.
    #     if (self.sender.get_possible_amount() - self.amount) < 0:
    #         log.warning(_(u'Balance limit of {} is reached. Limit is:'.format(self.sender, self.sender.get_possible_amount())))
    #         raise ValidationError('Balance limit is reached.')


    def __unicode__(self):
        return u"{} -> {}".format(self.sender, self.receiver)

def create_customer_account(sender, **kwargs):
    # use the user instance to create a new account if it not already exists
    user_account = kwargs.get('instance', None)
    if not user_account.bank_account.all():
        Account.objects.create(customer=user_account)


post_save.connect(create_customer_account, sender=settings.AUTH_USER_MODEL, dispatch_uid="create_user_profile")


def create_transfer(sender_account, receiver_account, amount, message):
    assert isinstance(sender_account, Account)
    assert isinstance(receiver_account, Account)
    transfer = Transfer()
    transfer.sender = sender_account
    transfer.receiver = receiver_account
    transfer.amount = amount
    transfer.save()

    return transfer


def execute_transfer(sender, **kwargs):
    # uses a signal to execute the transfer right after saving
    instance = kwargs.get('instance', False)

    if not instance:
        raise 'Fatal: Instance is not available.'

    if not instance.executed:
        amount = instance.amount
        sender = instance.sender
        receiver = instance.receiver

        sender.balance -= amount
        receiver.balance += amount

        sender.save()
        receiver.save()

        instance.executed = True
        instance.save()


post_save.connect(execute_transfer, sender=Transfer, dispatch_uid="execute_account_transfer")