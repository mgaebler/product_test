# coding: utf8
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


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


class Participation(models.Model):
    pass


class Invite(models.Model):
    pass


class ProductTest(models.Model):
    slug = models.SlugField(max_length=254, db_index=True)
    title = models.CharField(max_length=254)
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
    ends_at = models.DateTimeField(default=timezone.now, null=True)
    activated_at = models.DateTimeField(default=timezone.now, null=True)

    state = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_test_index', kwargs={'slug' : self.slug})