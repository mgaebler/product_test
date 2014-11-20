# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='address1',
            field=models.CharField(max_length=254, verbose_name='address1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='address2',
            field=models.CharField(max_length=254, null=True, verbose_name='address2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='address3',
            field=models.CharField(max_length=254, null=True, verbose_name='address3', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'', null=True, verbose_name='avatar', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='birth date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='city',
            field=models.CharField(max_length=254, verbose_name='city'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='country',
            field=models.CharField(max_length=254, verbose_name='country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='family_status',
            field=models.CharField(max_length=2, verbose_name='family status', choices=[(b'si', 'single'), (b'pa', 'partnership'), (b'ma', 'married'), (b'di', 'divorced'), (b'an', 'another')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(max_length=1, verbose_name='gender', choices=[(b'm', 'male'), (b'f', 'female'), (b'o', 'something else')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='postcode',
            field=models.CharField(max_length=12, null=True, verbose_name='postcode', blank=True),
            preserve_default=True,
        ),
    ]
