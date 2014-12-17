# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0006_auto_20141205_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttest',
            name='state',
            field=models.CharField(default='draft', help_text="\n            Draft: The product test is not visible to everyone.\n            Published: The Product test is visible if the 'published at' date is arrived.\n            Preview: The Product is visible to every staff member independently of the 'publishing at' date.\n        ", max_length=16, choices=[('draft', 'draft'), ('published', 'published'), ('preview', 'preview')]),
            preserve_default=True,
        ),
    ]
