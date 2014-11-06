# coding: utf8

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


class UserAccount(AbstractEmailUser):
    GENDER_CHOICES = (
        ('m', _('male')),
        ('f', _('female')),
        ('-', _('something else')),
    )
    FAMILY_STATUS_CHOICES = (
        ('si', _('single')),
        ('pa', _('partnership')),
        ('ma', _('married')),
        ('di', _('divorced')),
        ('an', _('another')),
    )

    # profile
    full_name = models.CharField('full name', max_length=255, blank=True)
    preferred_name = models.CharField('preferred name', max_length=255, blank=True)
    invited_by = models.ForeignKey("self", blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    avatar = ThumbnailerImageField(blank=True, null=True)
    avatar_url = models.URLField(max_length=254, null=True, blank=True)
    # todo: mindestalter?
    birth_date = models.DateField(blank=True, null=True)
    #address
    city = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    address1 = models.CharField(max_length=254)
    address2 = models.CharField(max_length=254, blank=True, null=True)
    address3 = models.CharField(max_length=254, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    family_status = models.CharField(choices=FAMILY_STATUS_CHOICES, max_length=2)

    registration_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=254, blank=True, null=True)
    confirmation_at = models.DateTimeField(blank=True, null=True)
    # use this to identify friend invites
    invite_token = models.CharField(max_length=254, blank=True, null=True, default=generate_token())
    profile_complete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.preferred_name

    def __unicode__(self):
        return "{} ({})".format(self.full_name, self.email)

