# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20141117_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='description',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
    ]
