# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20170618_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='number',
            new_name='gid',
        ),
    ]
