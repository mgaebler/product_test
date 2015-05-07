# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_adds_user_to_form_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='position',
            field=models.IntegerField(default=10, verbose_name='Position'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, verbose_name='Slug'),
            preserve_default=True,
        ),
    ]
