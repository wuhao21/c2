# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Group(models.Model):
    number = models.PositiveIntegerField(blank=False, unique=True)
    cipher = models.TextField(blank=False, default='Nonparticipator')

    def __unicode__(self):
            return "%d"%self.number

