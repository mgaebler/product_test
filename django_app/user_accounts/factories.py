# coding: utf8

import factory
from . import models


class TrendsetterUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserAccount

    email = 'info@trendsetter.eu'
    preferred_name = 'trendsetter'