# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0002_auto_20141107_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttest',
            name='link',
            field=models.URLField(default=' ', max_length=254),
            preserve_default=False,
        ),
    ]
