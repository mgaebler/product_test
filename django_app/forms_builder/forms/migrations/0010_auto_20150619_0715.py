# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import forms_builder.forms.models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_auto_20150612_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Position', blank=True),
            preserve_default=True,
        ),
    ]
