# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_auto_20141126_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqentry',
            name='position',
            field=models.PositiveSmallIntegerField(),
            preserve_default=True,
        ),
    ]
