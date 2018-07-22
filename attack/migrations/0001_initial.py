# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('attacker', models.CharField(default='ROOT', max_length=20)),
                ('defender', models.CharField(default='ROOT', max_length=20)),
                ('whom', models.CharField(blank=True, max_length=20)),
                ('atype', models.CharField(blank=True, max_length=20)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, default='NONE')),
                ('output', models.TextField(blank=True, default='NONE')),
                ('key', models.TextField(blank=True, default='NONE')),
                ('result', models.CharField(default='NONE', max_length=20)),
            ],
        ),
    ]
