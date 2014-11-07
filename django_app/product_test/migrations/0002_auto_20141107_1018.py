# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttest',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='product_test.Participation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participation',
            name='product_test',
            field=models.ForeignKey(to='product_test.ProductTest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participation',
            name='users',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
