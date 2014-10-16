# coding: utf8
import factory

from . import models


class ProductTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductTest

    title = factory.Sequence(lambda n: "TestTitle #%s" % n)
    slug = factory.Sequence(lambda n: "test_title_%s" % n)
