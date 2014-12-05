# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_test', '0004_auto_20141124_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
                ('product_test', models.OneToOneField(to='product_test.ProductTest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
