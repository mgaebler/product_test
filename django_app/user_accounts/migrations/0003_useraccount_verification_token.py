# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_useraccount_registration_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='verification_token',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
    ]
