# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'shop')),
                ('value', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
