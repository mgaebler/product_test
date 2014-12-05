# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20141110_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='teaser_image',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(max_length=255),
            preserve_default=True,
        ),
    ]
