# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FaqGroup(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.name


class FaqEntry(models.Model):
    group = models.ForeignKey(FaqGroup)
    question = models.TextField()
    answer = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.question


