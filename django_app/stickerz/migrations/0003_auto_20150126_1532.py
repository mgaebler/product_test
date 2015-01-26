# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerz', '0002_auto_20150126_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickercontainer',
            name='identifier',
            field=models.CharField(max_length=24),
            preserve_default=True,
        ),
    ]
