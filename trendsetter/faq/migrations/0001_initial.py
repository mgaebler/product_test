# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', markupfield.fields.MarkupField()),
                ('question_markup_type', models.CharField(default=None, max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')])),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('_question_rendered', models.TextField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FaqGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'FAQ name',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='faqentry',
            name='group',
            field=models.ForeignKey(to='faq.FaqGroup'),
            preserve_default=True,
        ),
    ]
