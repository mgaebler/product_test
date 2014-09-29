# coding: utf8

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Account(models.Model):
    CURRENCY_CHOICES = (('tp', 'Trend Points'),)
    TYPE_CHOICES = (
        ('ha', 'House account'),
        ('ca', 'Customer account'),
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='ca')
    description = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(User, related_name='bank_account')
    balance = models.IntegerField(default=0)
    currency = models.CharField(max_length=6, choices=CURRENCY_CHOICES, default='tp')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def debit(self, account):
        pass

    def credit(self, account):
        pass

    def validate_balance(self):
        pass

    def __unicode__(self):
        return "{customer} / {name}".format(customer=self.customer, name=self.name)


class Transfer(models.Model):
    sender = models.ForeignKey(Account, related_name="sender")
    receiver = models.ForeignKey(Account, related_name="receiver")
    reference = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(default=0)
    executed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


def create_user_account(sender, **kwargs):
    # use the user instance to create a new account
    Account.objects.create(customer=kwargs.get('instance', None))

post_save.connect(create_user_account, sender=User, dispatch_uid="create_user_profile")


def execute_transfer(sender, **kwargs):
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