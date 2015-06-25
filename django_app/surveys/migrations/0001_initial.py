# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Titel')),
                ('url', models.URLField(help_text="Die URL der Online-Umfrage, wie diese bei https://www.umfrageonline.com\n                     unter 'Umfrage bearbeiten' angezeigt wird. Z.B.: https://www.umfrageonline.com/s/92b3289", verbose_name='URL')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurveyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=50, verbose_name='Eindeutige ID')),
                ('survey', models.ForeignKey(to='surveys.Survey')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='survey',
            name='users',
            field=models.ManyToManyField(db_constraint='G\xfcltige Benutzer f\xfcr diese Umfrage', through='surveys.SurveyUser', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
