# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 19:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0067_auto_20171121_1050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Action',
            new_name='ReviewAction',
        ),
        migrations.RenameField(
            model_name='preprintservice',
            old_name='reviews_state',
            new_name='machine_state',
        ),
    ]
