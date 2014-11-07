# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_simple_forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='creator',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='topic',
            name='forum',
            field=models.ForeignKey(to='django_simple_forum.Forum'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(to='django_simple_forum.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forum',
            name='creator',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
