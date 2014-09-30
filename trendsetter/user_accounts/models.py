# coding: utf8

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
        ('-', 'something else'),
    )
    # profile
    # user = models.OneToOneField()
    invited_by = models.ForeignKey("self", blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    nickname = models.CharField(max_length=254)
    avatar = models.ImageField()
    avatar_url = models.URLField(max_length=254)
    birth_date = models.DateField(blank=True, null=True)
    #address
    city = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    address1 = models.CharField(max_length=254)
    address2 = models.CharField(max_length=254)
    address3 = models.CharField(max_length=254)
    postcode = models.IntegerField(blank=True, null=True)

    # invited_by = models.ForeignKey()

    confirmation_token = models.CharField(max_length=254)
    confirmation_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


