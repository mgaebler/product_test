# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20150611_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='status',
            field=models.IntegerField(default=1, verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')]),
            preserve_default=True,
        ),
    ]
