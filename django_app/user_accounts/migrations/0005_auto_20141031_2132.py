# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0004_auto_20141030_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='confirmation_token',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='invite_token',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
    ]
