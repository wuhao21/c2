# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MainPage(models.Model) :
    title = models.CharField(max_length = 50, unique = True)
    content = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.title
