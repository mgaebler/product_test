# coding: utf8

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
        ('-', 'something else'),
    )
    # profile
    user = models.OneToOneField(User)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    nickname = models.CharField(max_length=254)
    avatar = models.FileField()
    avatar_url = models.URLField()
    birth_date = models.DateField()
    #address
    city = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    address1 = models.CharField(max_length=254)
    address2 = models.CharField(max_length=254)
    address3 = models.CharField(max_length=254)
    postcode = models.IntegerField()

    # invited_by = models.ForeignKey()

    confirmation_token = models.CharField(max_length=254)
    confirmation_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


