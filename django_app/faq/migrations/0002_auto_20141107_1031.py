# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqentry',
            name='_answer_rendered',
        ),
        migrations.RemoveField(
            model_name='faqentry',
            name='_question_rendered',
        ),
        migrations.RemoveField(
            model_name='faqentry',
            name='answer_markup_type',
        ),
        migrations.RemoveField(
            model_name='faqentry',
            name='question_markup_type',
        ),
        migrations.AddField(
            model_name='faqentry',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faqentry',
            name='answer',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faqentry',
            name='question',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
