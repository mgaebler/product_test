# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='invited_by',
            field=models.ForeignKey(related_name=b'invited_by', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
