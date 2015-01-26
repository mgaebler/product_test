# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sticker',
            old_name='link',
            new_name='target_url',
        ),
    ]
