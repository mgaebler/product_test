# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.utils.timezone import utc
import datetime
import django.utils.timezone
from django.conf import settings
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0002_gallery_photographer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='photographer',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='is_checked',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='orig_file',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='creation_date',
            field=models.DateTimeField(default=gallery.models.utc_now, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='owner',
            field=models.ForeignKey(related_name='image_owner', on_delete=django.db.models.deletion.SET_NULL, verbose_name='owner', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='galleryvideo',
            name='link',
            field=models.URLField(default=datetime.datetime(2014, 11, 10, 15, 4, 25, 137727, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryvideo',
            name='owner',
            field=models.ForeignKey(related_name='video_owner', on_delete=django.db.models.deletion.SET_NULL, verbose_name='video_owner', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='file',
            field=models.ImageField(upload_to=b'galleries/%Y-%m-%d/', max_length=255, verbose_name='image file'),
            preserve_default=True,
        ),
    ]
