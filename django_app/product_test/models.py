# coding: utf-8
import logging
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models.signals import post_save

from django_simple_forum.models import Forum
from faq.models import FaqGroup
from gallery.models import Gallery


log = logging.getLogger('product_test')


class Brand(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, db_index=True)
    url = models.URLField()
    logo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'slug': self.slug})


class ProductTest(models.Model):
    slug = models.SlugField(max_length=254, db_index=True)
    title = models.CharField(max_length=254)
    link = models.URLField(max_length=254)
    brand = models.ForeignKey(Brand, null=True, blank=True)
    # Images
    hero_image = models.ImageField(null=True, blank=True)
    hero_image_url = models.URLField(null=True, blank=True)
    list_image = models.ImageField(null=True, blank=True)
    list_image_url = models.URLField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    # Customization
    custom_html = models.TextField(null=True, blank=True)
    custom_css = models.TextField(null=True, blank=True)
    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    activated_at = models.DateTimeField(default=timezone.now, null=True)

    faq = models.OneToOneField(FaqGroup, null=True, blank=True)
    gallery = models.OneToOneField(Gallery, null=True, blank=True)
    forum = models.OneToOneField(Forum, null=True, blank=True)

    state = models.BooleanField(default=False)

    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Participation")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_test:index', kwargs={'slug': self.slug})


class Participation(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL)
    product_test = models.ForeignKey(ProductTest)
    created_at = models.DateTimeField(auto_now_add=True)


class TestResult(models.Model):
    product_test = models.OneToOneField(ProductTest)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __unicode__(self):
        return self.title


def create_product_test_add_ons(sender, **kwargs):
    # use the user instance to create a new account if it not already exists
    product_test = kwargs.get('instance', None)
    if not product_test.faq:
        product_test.faq = FaqGroup.objects.create(
            name=u"{name}-faq".format(name=product_test.title),
            text=u" "
        )
        product_test.save()

    if not product_test.gallery:
        product_test.gallery = Gallery.objects.create(name=u"{name}-gallery".format(name=product_test.title))
        product_test.save()

    if not product_test.forum:
        product_test.forum = Forum.objects.create(title=u"{name}-forum".format(name=product_test.title))
        product_test.save()
    # import pudb; pu.db


post_save.connect(create_product_test_add_ons, sender=ProductTest, dispatch_uid="create_product_test_subs")