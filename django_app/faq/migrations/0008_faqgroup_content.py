# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0007_auto_20150127_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqgroup',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
