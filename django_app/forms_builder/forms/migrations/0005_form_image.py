# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_adds_trendpoints_to_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Image', blank=True),
            preserve_default=True,
        ),
    ]
