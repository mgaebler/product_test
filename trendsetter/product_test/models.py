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
    hero_image = models.FileField()
    hero_image_url = models.URLField()
    list_image = models.FileField()
    list_image_url = models.URLField()
    logo = models.FileField()
    logo_url = models.URLField()
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