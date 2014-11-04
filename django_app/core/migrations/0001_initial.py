# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_initial_house_accounts(apps, schema_editor):
    Account = apps.get_model("simple_bank", "Account")
    Account.objects.create(
        name='trendsetter',
        description='The app house account.',
        type='ha'
    )

    Account.objects.create(
        name='shop',
        description='The shop house account.',
        type='ha'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bank', '0005_auto_20141103_1033'),
    ]

    operations = [
        migrations.RunPython(add_initial_house_accounts),
    ]
