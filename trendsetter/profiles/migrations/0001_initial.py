# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'male'), (b'f', b'female'), (b'-', b'something else')])),
                ('nickname', models.CharField(max_length=254)),
                ('avatar', models.FileField(upload_to=b'')),
                ('avatar_url', models.URLField()),
                ('birth_date', models.DateField()),
                ('city', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('status', models.CharField(max_length=254)),
                ('address1', models.CharField(max_length=254)),
                ('address2', models.CharField(max_length=254)),
                ('address3', models.CharField(max_length=254)),
                ('postcode', models.IntegerField()),
                ('confirmation_token', models.CharField(max_length=254)),
                ('confirmation_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
