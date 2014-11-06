# coding: utf8
import factory
from PIL import Image
from StringIO import StringIO
from django.core.files.base import ContentFile
from product_test import models


def create_image():
    image_file = StringIO()
    image = Image.new('RGBA', size=(50,50), color=(256,0,0))
    image.save(image_file, 'png')
    image_file.seek(0)

    return ContentFile(image_file.read(), 'test.png')


class ProductTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductTest

    title = factory.Sequence(lambda n: "TestTitle #%s" % n)
    slug = factory.Sequence(lambda n: "test-title-%s" % n)
    hero_image = create_image()
    list_image = create_image()
    logo = create_image()