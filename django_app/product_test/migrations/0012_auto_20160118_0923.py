# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0011_brand_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttest',
            name='participants_file',
            field=models.FileField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producttest',
            name='trendpoints_file',
            field=models.FileField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
