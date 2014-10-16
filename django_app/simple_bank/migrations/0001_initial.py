# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('type', models.CharField(default=b'ca', max_length=2, choices=[(b'ha', b'House account'), (b'ca', b'Customer account')])),
                ('description', models.TextField(null=True, blank=True)),
                ('balance', models.IntegerField(default=0)),
                ('currency', models.CharField(default=b'tp', max_length=6, choices=[(b'tp', b'Trend Points')])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(max_length=255, null=True, blank=True)),
                ('amount', models.IntegerField(default=0)),
                ('executed', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(related_name=b'receiver', to='simple_bank.Account')),
                ('sender', models.ForeignKey(related_name=b'sender', to='simple_bank.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
