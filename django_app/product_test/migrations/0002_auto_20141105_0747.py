# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0001_initial'),
        ('gallery', '0001_initial'),
        ('faq', '0001_initial'),
        ('product_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttest',
            name='faq',
            field=models.OneToOneField(null=True, blank=True, to='faq.FaqGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producttest',
            name='forum',
            field=models.OneToOneField(null=True, blank=True, to='django_simple_forum.Forum'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producttest',
            name='gallery',
            field=models.OneToOneField(null=True, blank=True, to='gallery.Gallery'),
            preserve_default=True,
        ),
    ]
