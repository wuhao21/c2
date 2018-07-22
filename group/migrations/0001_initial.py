# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('gid', models.CharField(max_length=10, unique=True)),
                ('username', models.CharField(default='ROOT', max_length=50)),
                ('cipher', models.TextField(default='ciphertext')),
                ('plaintext', models.TextField(default='plaintext')),
                ('score', models.FloatField(default=5)),
            ],
        ),
    ]
