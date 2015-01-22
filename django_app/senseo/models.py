# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class SEOData(models.Model):
    """
    Add SEO-related fields to your model by adding a foreign key to this model.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    title_tag = models.CharField(max_length=45, )
    meta_description = models.TextField(u'META Beschreibung', max_length=156, blank=True, null=True)
    meta_keywords = models.TextField(
        u'META Keywords', blank=True, null=True, help_text=u'Keywords durch Komma trennen')
    canonical_url = models.URLField(
        u'Canonical URL', blank=True, null=True, help_text=u'Nur angeben wenn abweichend von original URL.')
    noindex = models.BooleanField(u'Nicht indizieren?', default=False)

    class Meta:
        verbose_name = u'SEO-Daten'
        verbose_name_plural = u'SEO-Daten'
