# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_adds_position_to_form'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='form',
            options={'ordering': ('position',), 'verbose_name': 'Form', 'verbose_name_plural': 'Forms'},
        ),
        migrations.AddField(
            model_name='form',
            name='trendpoints',
            field=models.IntegerField(default=10, verbose_name='Trendpoints'),
            preserve_default=True,
        ),
    ]
