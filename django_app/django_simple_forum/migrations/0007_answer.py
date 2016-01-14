# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_simple_forum', '0006_auto_20150127_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('body', models.TextField(max_length=10000, verbose_name='body')),
                ('user_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('creator', models.ForeignKey(verbose_name='creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('post', models.ForeignKey(related_name='answers', verbose_name='topic', to='django_simple_forum.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
