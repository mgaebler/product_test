# coding: utf-8

import factory
from . import models


class product-testUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserAccount

    email = 'info@product-test.eu'
    preferred_name = 'product-test'