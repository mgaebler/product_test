# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
        ('product_test', '0008_brand_logo_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttest',
            name='application_survey',
            field=models.ForeignKey(related_name='application_survey', blank=True, to='surveys.Survey', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producttest',
            name='completion_survey',
            field=models.ForeignKey(related_name='completion_survey', blank=True, to='surveys.Survey', null=True),
            preserve_default=True,
        ),
    ]
