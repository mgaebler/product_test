# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0007_auto_20141217_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(upload_to=b'', verbose_name='Logo overview'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='logo_top',
            field=models.ImageField(help_text='\n        When this logo is given, the default trendsetter logo on top left of the\n        page is exchanged with this one on all product test pages.', null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
