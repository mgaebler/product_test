# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0003_auto_20141121_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='birth date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='full name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='postcode',
            field=models.CharField(max_length=12, null=True, verbose_name='postcode'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='preferred_name',
            field=models.CharField(max_length=255, verbose_name='preferred name'),
            preserve_default=True,
        ),
    ]
