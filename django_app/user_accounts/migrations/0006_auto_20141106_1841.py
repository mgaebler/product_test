# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0005_auto_20141031_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='status',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='invite_token',
            field=models.CharField(default=b'86eaaa1a026493e17c18275f048ab65ac2218311', max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
    ]
