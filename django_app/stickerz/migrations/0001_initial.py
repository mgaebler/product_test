# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('link', models.URLField(max_length=510, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'stickerz')),
                ('position', models.PositiveSmallIntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='modification_date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StickerContainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=12)),
                ('description', models.TextField(help_text='Say something about this container. For example where it lives.')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('template', models.CharField(help_text=b'Optional: A template corresponding to your container format.', max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sticker',
            name='container',
            field=models.ForeignKey(related_name='stickers', to='stickerz.StickerContainer'),
            preserve_default=True,
        ),
    ]
