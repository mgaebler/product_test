# coding: utf-8
import datetime
import logging

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)


class Gallery(models.Model):
    name = models.CharField(_(u'name'), max_length=255)
    slug = models.SlugField(_(u'slug'), max_length=255)

    description = models.TextField(verbose_name=_('description'), help_text=_('gallery_gallery_description_help_text'),
                                   blank=True, null=True)
    teaser_image = models.ImageField(_(u'teaser image'), upload_to='galleries/teaser/%Y-%m-%d/', max_length=255)

    is_deleted = models.BooleanField(verbose_name=_('is_deleted'), default=False)

    active = models.BooleanField(verbose_name=_('published'), default=True)
    publish_date = models.DateTimeField(
        verbose_name=_('publish_date'),
        default=datetime.datetime.utcnow().replace(tzinfo=utc)
    )

    photographer = models.ForeignKey(
        User, verbose_name=_('photographer'),
        related_name='gallery_photographer',
        null=True, on_delete=models.SET_NULL
    )

    creation_date = models.DateTimeField(default=datetime.datetime.utcnow().replace(tzinfo=utc), editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    def delete(self, using=None):
        self.is_deleted = True
        self.save()


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')

    orig_file = models.ImageField(
        verbose_name=_('original file'),
        upload_to='galleries/%Y-%m-%d/original/',
        max_length=255,
        width_field='width',
        height_field='height',
        help_text=_('gallery_galleryimage_file_help_text')
    )

    file = models.ImageField(
        verbose_name=_('800 x 600 image file'),
        upload_to='galleries/%Y-%m-%d/',
        max_length=255,
        width_field='width',
        height_field='height',
        help_text=_('gallery_galleryimage_file_help_text'),
        db_index=True
    )

    is_deleted = models.BooleanField(verbose_name=_('is_deleted'), default=False)
    is_checked = models.BooleanField(verbose_name=_('is_checked'), default=False)

    class Meta():
        verbose_name = _('gallery_image')
        verbose_name_plural = _('gallery_images')
        position_filter = 'gallery'
        ordering = ('position_in_gallery',)
        unique_together = (
            ('portal', 'legacy_id'),
        )
        index_together = (
            ('gallery', 'position_in_gallery'),
        )


class GalleryVideo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='videos')