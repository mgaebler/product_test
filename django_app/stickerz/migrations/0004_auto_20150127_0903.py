# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerz', '0003_auto_20150126_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sticker',
            options={'ordering': ['position']},
        ),
    ]
