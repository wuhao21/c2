# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 07:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20170618_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainpage',
            old_name='cotent',
            new_name='content',
        ),
    ]
