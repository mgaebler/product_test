# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_accounts.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_auto_20141120_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=user_accounts.models.get_avatar_upload_path, null=True, verbose_name='avatar', blank=True),
            preserve_default=True,
        ),
    ]
