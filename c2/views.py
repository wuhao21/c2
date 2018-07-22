# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os
f = open('index.md')
content = f.read()

def index(request):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'new', 'username':''})
    return render(request, 'index.html', {'content':content, 'status' : 'in', 'username': username})


