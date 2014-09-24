# coding: utf8
from django.db import models


class Brands(models.Model):
    pass


class Participations(models.Model):
    pass


class Invites(models.Model):
    pass


class ProductTest(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    brand = models.ForeignKey(Brands)
    # Images
    hero_image = models.ImageField(null=True, blank=True)
    hero_image_url = models.URLField(null=True, blank=True)
    list_image = models.ImageField(null=True, blank=True)
    list_image_url = models.URLField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    # Customization
    custom_html = models.TextField()
    custom_css = models.TextField()
    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    activated_at = models.DateTimeField()

    state = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

