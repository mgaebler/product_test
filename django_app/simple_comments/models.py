# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from static_pages.models import FlatPage


class Comment(models.Model):
    title = models.CharField(_(u'title'), max_length=255)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'creator'), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    body = models.TextField(verbose_name=_(u'body'), max_length=10000)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    # TODO: Remove flatpage once the existing commments are migrated
    flatpage = models.ForeignKey(FlatPage, blank=True, null=True, related_name='comments')

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey()

    def __unicode__(self):
        return u"{}".format(self.title)

    class Meta:
        ordering = ('-created',)
