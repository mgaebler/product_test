# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FaqGroup(models.Model):
    STATE_PUBLISHED = 'published'
    STATE_PREVIEW = 'preview'
    STATE_DEACTIVATED = 'deactivated'
    STATES = (
        (STATE_PUBLISHED, _(u'published')),
        (STATE_PREVIEW, _(u'preview')),
        (STATE_DEACTIVATED, _(u'deactivated')),
    )
    name = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=24, choices=STATES, default=u'published',
        help_text=u"""
            Draft: The product test is not visible to everyone.
            Published: The Product test is visible if the 'published at' date is arrived.
            Preview: The Product is visible to every staff member independently of the 'publishing at' date.
        """
    )
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


