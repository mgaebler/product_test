# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20150612_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='choices',
            field=models.CharField(help_text='Comma separated options where applicable. If an option itself contains commas, surround the option starting with the `character and ending with the ` character.', max_length=2000, verbose_name='Choices', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='help_text',
            field=models.CharField(max_length=2000, verbose_name='Help text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='label',
            field=models.CharField(max_length=2000, verbose_name='Label'),
            preserve_default=True,
        ),
    ]
