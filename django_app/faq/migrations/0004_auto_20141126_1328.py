# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_auto_20141121_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqentry',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='faqentry',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Position'),
            preserve_default=False,
        ),
    ]
