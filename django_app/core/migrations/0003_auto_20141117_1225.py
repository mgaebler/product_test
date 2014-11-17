# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_initial_static_pages(apps, schema_editor):
    StaticPage = apps.get_model("core", "StaticPage")
    pages = (
        # ('Name', 'Slug', 'Description', 'Content'),
        ('Agb', '/agb', '', ''),
        ('Datenschutz', '/datenschutz', '', ''),
        ('FAQ', '/faq', '', ''),
        ('Impressum', '/impressum', '', ''),
        ('Partnerinfo', '/partnerinfo', '', ''),
        ('Teilnahmebedingungen', '/teilnahmebedingungen', '', ''),
        ('Über Uns', '/ueber-uns', '', ''),
        ('Unsere Marken', '/unsere-marken', '', ''),
        ('Wie funktioniert es', '/wie-funktioniert-es', '', ''),
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
        ('core', '0002_staticpage'),
    ]

    operations = [
        migrations.RunPython(add_initial_static_pages),
    ]
