# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_initial_static_pages(apps, schema_editor):
    StaticPage = apps.get_model("core", "StaticPage")
    pages = (
        # ('Name', 'Slug', 'Description', 'Content'),
        ('Index', '/', '', ''),
    )

    for page in pages:
        StaticPage.objects.create(
            name=page[0],
            slug=page[1],
            description=page[2],
            content=page[3]
        )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141117_1225'),
    ]

    operations = [
        migrations.RunPython(add_initial_static_pages),
    ]
