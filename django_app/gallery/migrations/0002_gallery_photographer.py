# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='photographer',
            field=models.ForeignKey(related_name='gallery_photographer', on_delete=django.db.models.deletion.SET_NULL, verbose_name='photographer', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
