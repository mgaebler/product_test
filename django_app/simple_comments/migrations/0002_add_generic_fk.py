# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('simple_comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
