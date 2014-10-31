# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bank', '0002_account_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='reference',
            field=models.CharField(help_text='A short description of what why you did this.', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
