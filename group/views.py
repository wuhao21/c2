# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from group.models import Group
import os
f = open('indexmd.txt')
content = f.read()
f.close()

# Create your views here.

def readme(request, gid):
    request.encoding='utf-8'
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    try:
        group = Group.objects.get(gid=gid)
    except Group.DoesNotExist:
        raise Http404
    f = open("data/%s/README"%gid)
    content = f.read()
    f.close()
    return HttpResponse(content)

def generate(request, gid):
    request.encoding='utf-8'
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    try:
        group = Group.objects.get(gid=gid)
    except Group.DoesNotExist:
        raise Http404
    temp_file = os.popen("data/%s/c2 --generate"%gid)
    key = temp_file.read()
    temp_file.close()
    return HttpResponse(key)

def detail(request, gid):
    try:
        username = request.session['who']
    except KeyError:
	return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    try:
        group = Group.objects.get(gid=gid)
    except Group.DoesNotExist:
        raise Http404
    return render(request, 'group/detail.html', {'group' : group, 'username' : username, 'readme' : ""})
