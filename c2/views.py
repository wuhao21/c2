# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os
f = open('indexmd.txt')
content = f.read()

def index(request):
	return render(request, 'index.html', {'content':content, 'status' : 'new', 'username': ''})

