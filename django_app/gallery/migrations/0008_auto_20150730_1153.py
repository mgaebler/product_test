# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20150127_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title', blank=True),
            preserve_default=True,
        ),
    ]
