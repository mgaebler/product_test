# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141117_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='slug',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
    ]
