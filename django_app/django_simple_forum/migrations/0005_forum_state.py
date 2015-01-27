# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0004_auto_20141205_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='state',
            field=models.CharField(default='published', help_text="\n            Draft: The product test is not visible to everyone.\n            Published: The Product test is visible if the 'published at' date is arrived.\n            Preview: The Product is visible to every staff member independently of the 'publishing at' date.\n        ", max_length=24, choices=[(b'published', 'published'), (b'preview', 'preview')]),
            preserve_default=True,
        ),
    ]
