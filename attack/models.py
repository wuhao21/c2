# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Attack(models.Model):
    attacker = models.CharField(max_length=20, blank=False, default='ROOT')
    whom = models.CharField(max_length=20, blank=True)
    atype = models.CharField(max_length=10, blank=True)
    date_time = models.DateTimeField(auto_now_add = True)
    text = models.TextField(blank = True, default='NONE')
    result = models.TextField(blank = True, default='NONE')
    key = models.TextField(blank = True, default='NONE')
    def __unicode__(self) :
        return "%d"%self.id

