# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from markupfield.fields import MarkupField


class FaqGroup(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)


class FaqEntry(models.Model):
    group = models.ForeignKey(FaqGroup)
    question = MarkupField()
    #answer = MarkupField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True, editable=False)


