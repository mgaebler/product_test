# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bank', '0004_account_overdraft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(related_name='bank_account', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
