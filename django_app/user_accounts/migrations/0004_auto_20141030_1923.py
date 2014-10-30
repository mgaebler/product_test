# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0003_useraccount_verification_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='verification_token',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='invite_token',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile_complete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
