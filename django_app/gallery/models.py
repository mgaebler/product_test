# coding: utf-8
import datetime
import logging

from user_accounts.models import UserAccount as User
from django.db import models
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)

def utc_now():
    return datetime.datetime.utcnow().replace(tzinfo=utc)


class Gallery(models.Model):
    STATE_PUBLISHED = 'published'
    STATE_PREVIEW = 'preview'
    STATE_DEACTIVATED = 'deactivated'
    STATES = (
        (STATE_PUBLISHED, _(u'published')),
        (STATE_PREVIEW, _(u'preview')),
        (STATE_DEACTIVATED, _(u'deactivated'))
    )
    name = models.CharField(_(u'name'), max_length=255)
    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('gallery_gallery_description_help_text'),
        blank=True,
        null=True
    )
    state = models.CharField(max_length=24, choices=STATES, default=u'published',
        help_text=u"""
            Draft: The product test is not visible to everyone.
            Published: The Product test is visible if the 'published at' date is arrived.
            Preview: The Product is visible to every staff member independently of the 'publishing at' date.
        """
    )
    active = models.BooleanField(verbose_name=_('published'), default=True)
    creation_date = models.DateTimeField(default=utc_now, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Galleries'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')
    file = models.ImageField(
        verbose_name=_('image file'),
        upload_to='galleries/%Y-%m-%d/',
        max_length=255
    )
    owner = models.ForeignKey(
        User, verbose_name=_('owner'),
        related_name='image_owner',
        null=True, on_delete=models.SET_NULL
    )

    creation_date = models.DateTimeField(default=utc_now, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)


class GalleryVideo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='videos')
    link = models.URLField()

    owner = models.ForeignKey(
        User, verbose_name=_('video_owner'),
        related_name='video_owner',
        null=True, on_delete=models.SET_NULL
    )

    def __unicode__(self):
        return self.link