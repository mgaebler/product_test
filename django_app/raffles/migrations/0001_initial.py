# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raffle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100, verbose_name='URL', db_index=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('enable_comments', models.BooleanField(default=False, verbose_name='enable comments')),
                ('logo', models.ImageField(upload_to=b'raffles', null=True, verbose_name='Logo', blank=True)),
                ('list_image', models.ImageField(upload_to=b'raffles', null=True, verbose_name='List Image', blank=True)),
                ('starts_at', models.DateTimeField(null=True, blank=True)),
                ('ends_at', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='raffle',
            options={'ordering': ('url',), 'verbose_name': 'raffle', 'verbose_name_plural': 'raffles'},
        ),
        migrations.AlterModelOptions(
            name='raffle',
            options={'ordering': ('starts_at', 'ends_at'), 'verbose_name': 'raffle', 'verbose_name_plural': 'raffles'},
        ),
    ]
