# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('description', models.TextField(help_text='gallery_gallery_description_help_text', null=True, verbose_name='description', blank=True)),
                ('teaser_image', models.ImageField(upload_to=b'galleries/teaser/%Y-%m-%d/', max_length=255, verbose_name='teaser image')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('active', models.BooleanField(default=True, verbose_name='published')),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2014, 11, 5, 7, 47, 31, 643083, tzinfo=utc), verbose_name='publish_date')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2014, 11, 5, 7, 47, 31, 643163, tzinfo=utc), editable=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('photographer', models.ForeignKey(related_name='gallery_photographer', on_delete=django.db.models.deletion.SET_NULL, verbose_name='photographer', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orig_file', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'galleries/%Y-%m-%d/original/', max_length=255, help_text='gallery_galleryimage_file_help_text', verbose_name='original file')),
                ('file', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'galleries/%Y-%m-%d/', max_length=255, help_text='gallery_galleryimage_file_help_text', verbose_name='800 x 600 image file', db_index=True)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('is_checked', models.BooleanField(default=False, verbose_name='is_checked')),
                ('gallery', models.ForeignKey(related_name='images', to='gallery.Gallery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gallery', models.ForeignKey(related_name='videos', to='gallery.Gallery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
