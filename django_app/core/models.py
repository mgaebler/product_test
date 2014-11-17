# coding: utf-8
from django.db import models


class StaticPage(models.Model):
    name = models.CharField(max_length=254)
    slug = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
