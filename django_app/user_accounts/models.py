# coding: utf-8

from authtools.models import AbstractEmailUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from hashlib import sha1


def generate_token():
    time = timezone.now().isoformat()
    token = sha1(time)
    return token.hexdigest()


def get_avatar_upload_path(instance, filename):
    return u"user/avatar/{}/{}".format(instance.id, filename)


class UserAccount(AbstractEmailUser):
    GENDER_CHOICES = (
        ('m', _('male')),
        ('f', _('female')),
        ('o', _('something else')),
    )
    FAMILY_STATUS_CHOICES = (
        ('si', _('single')),
        ('pa', _('partnership')),
        ('ma', _('married')),
        ('di', _('divorced')),
        ('an', _('another')),
    )

    # profile
    full_name = models.CharField(_('full name'), max_length=255, blank=True)
    preferred_name = models.CharField(_('preferred name'), max_length=255, blank=True)

    gender = models.CharField(_('gender'), choices=GENDER_CHOICES, max_length=1)
    avatar = ThumbnailerImageField(_('avatar'), upload_to=get_avatar_upload_path, blank=True, null=True)
    avatar_url = models.URLField(max_length=254, null=True, blank=True)
    # todo: mindestalter validieren?
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    #address
    city = models.CharField(_('city'), max_length=254)
    country = models.CharField(_('country'),max_length=254)
    address1 = models.CharField(_('address1'),max_length=254)
    address2 = models.CharField(_('address2'), max_length=254, blank=True, null=True)
    address3 = models.CharField(_('address3'), max_length=254, blank=True, null=True)
    postcode = models.CharField(_('postcode'), max_length=12, blank=True, null=True)
    family_status = models.CharField(_('family status'),choices=FAMILY_STATUS_CHOICES, max_length=2)

    invited_by = models.ForeignKey("self", blank=True, null=True)

    registration_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=254, blank=True, null=True)
    confirmation_at = models.DateTimeField(blank=True, null=True)
    # use this to identify friend invites
    invite_token = models.CharField(max_length=254, blank=True, null=True, default=generate_token)
    profile_complete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.preferred_name

    def __unicode__(self):
        return self.email

