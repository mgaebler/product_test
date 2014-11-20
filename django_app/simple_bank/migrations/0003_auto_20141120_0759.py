# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bank', '0002_account_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='overdraft',
            field=models.IntegerField(default=0, help_text='Du hast nicht gen\xfcgend Trendpoints, um die gew\xfcnschte Aktion auszuf\xfchren.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transfer',
            name='reference',
            field=models.CharField(help_text='Grund f\xfcr Trendpoint-Vergabe', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
