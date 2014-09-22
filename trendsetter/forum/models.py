# -*- coding: utf-8 -*-
from django.db import models
from markupfield.fields import MarkupField


class ForumGroup(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)


class ForumEntry(models.Model):
    group = models.ForeignKey(ForumGroup)
    question = MarkupField()
    #answer = MarkupField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return ''

