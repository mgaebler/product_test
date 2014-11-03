# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bank', '0003_auto_20141031_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='overdraft',
            field=models.IntegerField(default=0, help_text='Limit of overdraft the current account.'),
            preserve_default=True,
        ),
    ]
