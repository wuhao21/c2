# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
