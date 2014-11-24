# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0003_producttest_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttest',
            name='ends_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
