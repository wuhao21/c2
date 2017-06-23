# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from group.models import Group
import os
f = open('indexmd.txt')
content = f.read()

# Create your views here.

def detail(request, gid):
    try:
        username = request.session['who']
    except KeyError:
	return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    try:
        group = Group.objects.get(gid=gid)
    except Group.DoesNotExist:
        raise Http404
    return render(request, 'group/detail.html', {'group' : group, 'username' : username})
