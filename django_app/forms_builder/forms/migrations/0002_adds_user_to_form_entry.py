# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formentry',
            name='user',
            field=models.ForeignKey(related_name='forms', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='sites',
            field=models.ManyToManyField(default=[1], related_name='forms_form_forms', editable=False, to='sites.Site'),
            preserve_default=True,
        ),
    ]
