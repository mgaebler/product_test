# coding: utf8
import factory
from product_test import models


class ProductTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductTest

    title = factory.Sequence(lambda n: "TestTitle #%s" % n)
    slug = factory.Sequence(lambda n: "test-title-%s" % n)
    hero_image = factory.django.ImageField(color='green')
    list_image = factory.django.ImageField(color='blue')
    logo = factory.django.ImageField(color='red')


