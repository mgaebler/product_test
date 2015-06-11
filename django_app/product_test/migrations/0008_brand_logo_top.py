# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0007_auto_20141217_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo_top',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
