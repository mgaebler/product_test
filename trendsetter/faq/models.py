# -*- coding: utf-8 -*-
from django.db import models


class FaqGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = u'FAQ name'
        ordering = ('-published',)


class FaqEntry(models.Model):
    group = models.ForeignKey(FaqGroup)
    question = models.TextField()
    answer = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return ''

