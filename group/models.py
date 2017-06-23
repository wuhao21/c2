# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Group(models.Model):
    gid = models.CharField(max_length=10, blank=False, unique=True)
    cipher = models.TextField(blank=False, default='Nonparticipator')

    def __unicode__(self):
            return 'group%s'%self.gid

