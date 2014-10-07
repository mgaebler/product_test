# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address', db_index=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=255, verbose_name=b'full name', blank=True)),
                ('preferred_name', models.CharField(max_length=255, verbose_name=b'preferred name', blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', 'male'), (b'f', 'female'), (b'-', 'something else')])),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'', blank=True)),
                ('avatar_url', models.URLField(max_length=254, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('city', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('status', models.CharField(max_length=254)),
                ('address1', models.CharField(max_length=254)),
                ('address2', models.CharField(max_length=254, null=True, blank=True)),
                ('address3', models.CharField(max_length=254, null=True, blank=True)),
                ('postcode', models.IntegerField(null=True, blank=True)),
                ('family_status', models.CharField(max_length=2, choices=[(b'si', 'single'), (b'pa', 'partnership'), (b'ma', 'married'), (b'di', 'divorced'), (b'an', 'another')])),
                ('confirmation_token', models.CharField(max_length=254)),
                ('confirmation_at', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('invited_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['email'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
