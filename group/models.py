# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Group(models.Model):
    gid = models.CharField(max_length=10, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, default='ROOT')
    cipher = models.TextField(blank=False, default='ciphertext')
    plaintext = models.TextField(blank=False, default='plaintext')
    score = models.FloatField(default=5)

    def __unicode__(self):
            return 'group%s'%self.gid

