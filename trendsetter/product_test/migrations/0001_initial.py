# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('slug', models.SlugField(max_length=254)),
                ('url', models.URLField()),
                ('logo', models.ImageField(upload_to=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=254)),
                ('title', models.CharField(max_length=254)),
                ('hero_image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('hero_image_url', models.URLField(null=True, blank=True)),
                ('list_image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('list_image_url', models.URLField(null=True, blank=True)),
                ('logo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('logo_url', models.URLField(null=True, blank=True)),
                ('custom_html', models.TextField(null=True, blank=True)),
                ('custom_css', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('ends_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('activated_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('state', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(blank=True, to='product_test.Brand', null=True)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='product_test.Participation')),
            ],
            options={
            },
            bases=(models.Model,),
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
