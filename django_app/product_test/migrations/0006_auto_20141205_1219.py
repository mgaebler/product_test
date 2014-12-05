# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0005_testresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='product_test',
        ),
        migrations.AddField(
            model_name='producttest',
            name='test_result',
            field=models.OneToOneField(null=True, blank=True, to='product_test.TestResult'),
            preserve_default=True,
        ),
    ]
