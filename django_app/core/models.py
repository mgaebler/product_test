# coding: utf-8
from django.db import models


class StaticPage(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField()
    description = models.TextField()
    content = models.TextField()

    def __unicode__(self):
        return self.name
