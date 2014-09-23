# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=255)),
                ('hero_image', models.FileField(upload_to=b'')),
                ('hero_image_url', models.URLField()),
                ('list_image', models.FileField(upload_to=b'')),
                ('list_image_url', models.URLField()),
                ('logo', models.FileField(upload_to=b'')),
                ('logo_url', models.URLField()),
                ('custom_html', models.TextField()),
                ('custom_css', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('activated_at', models.DateTimeField()),
                ('state', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(to='product_test.Brands')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
