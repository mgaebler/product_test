# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0002_auto_20141107_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forum',
            name='creator',
            field=models.ForeignKey(verbose_name='creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.TextField(default=b'', verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forum',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=10000, verbose_name='body'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(verbose_name='creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(verbose_name='topic', to='django_simple_forum.Topic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='creator',
            field=models.ForeignKey(verbose_name='creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(max_length=10000, null=True, verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
            preserve_default=True,
        ),
    ]
