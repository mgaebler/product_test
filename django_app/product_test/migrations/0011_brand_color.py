# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0010_auto_20150716_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='color',
            field=models.CharField(default='fd7263', max_length=6, verbose_name='Color'),
            preserve_default=True,
        ),
    ]
