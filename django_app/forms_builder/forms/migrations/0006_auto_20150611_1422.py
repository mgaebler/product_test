# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_form_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='placeholder_text',
            field=models.CharField(verbose_name='Placeholder Text', max_length=100, null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='login_required',
            field=models.BooleanField(default=True, help_text='If checked, only logged in users can view the form', verbose_name='Login required'),
            preserve_default=True,
        ),
    ]
