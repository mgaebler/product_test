# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEOData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('title_tag', models.CharField(max_length=45)),
                ('meta_description', models.TextField(max_length=156, null=True, verbose_name='META Beschreibung', blank=True)),
                ('meta_keywords', models.TextField(help_text='Keywords durch Komma trennen', null=True, verbose_name='META Keywords', blank=True)),
                ('canonical_url', models.URLField(help_text='Nur angeben wenn abweichend von original URL.', null=True, verbose_name='Canonical URL', blank=True)),
                ('noindex', models.BooleanField(default=False, verbose_name='Nicht indizieren?')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'SEO-Daten',
                'verbose_name_plural': 'SEO-Daten',
            },
            bases=(models.Model,),
        ),
    ]
