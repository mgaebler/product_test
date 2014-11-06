# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 6, 17, 0, 11, 551302, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 6, 17, 0, 11, 551212, tzinfo=utc), verbose_name='publish_date'),
            preserve_default=True,
        ),
    ]
