# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20150612_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='placeholder_text',
            field=models.CharField(max_length=100, null=True, verbose_name='Placeholder Text', blank=True),
            preserve_default=True,
        ),
    ]
