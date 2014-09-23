#coding: utf8

from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    executed = models.BooleanField()


class Account(models.Model):
    CURRENCY_CHOICES = (('Trend Points', 'tp'),)
    TYPE_CHOICES = (
        ('House account', 'ha'),
        ('Customer account', 'ca'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='ca')
    description = models.TextField()
    customer = models.ForeignKey(User)
    balance = models.IntegerField(default=0)
    currency = models.CharField(max_length=6, choices=CURRENCY_CHOICES, default='tp')
    transactions = models.ForeignKey(Transaction)

    def debit(self, account):
        pass

    def credit(self, account):
        pass

    def validate_balance(self):
        pass

    def __unicode__(self):
        return "{ owner }/{name}".format(owner=self.owner, name=self.name)