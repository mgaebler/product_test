# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0009_auto_20150625_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttest',
            name='application_survey_end',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producttest',
            name='application_survey_start',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producttest',
            name='completion_survey_end',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producttest',
            name='completion_survey_start',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
