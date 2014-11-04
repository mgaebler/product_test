# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bank', '0005_auto_20141103_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='aborted',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
