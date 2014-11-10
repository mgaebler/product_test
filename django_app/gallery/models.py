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
    name = models.CharField(_(u'name'), max_length=255)
    slug = models.SlugField(_(u'slug'), max_length=255)

    description = models.TextField(
        verbose_name=_('description'),
        help_text=_('gallery_gallery_description_help_text'),
        blank=True,
        null=True
    )
    teaser_image = models.ImageField(_(u'teaser image'), upload_to='galleries/teaser/%Y-%m-%d/', max_length=255)
    is_deleted = models.BooleanField(verbose_name=_('is_deleted'), default=False)

    active = models.BooleanField(verbose_name=_('published'), default=True)
    publish_date = models.DateTimeField(
        verbose_name=_('publish_date'),
        default=utc_now
    )

    creation_date = models.DateTimeField(default=utc_now, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    def delete(self, using=None):
        self.is_deleted = True
        self.save()

    def __unicode__(self):
        return self.name


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
    is_deleted = models.BooleanField(verbose_name=_('is_deleted'), default=False)


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