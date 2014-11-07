# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20141106_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 6, 18, 41, 37, 413974, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 6, 18, 41, 37, 413874, tzinfo=utc), verbose_name='publish_date'),
            preserve_default=True,
        ),
    ]
