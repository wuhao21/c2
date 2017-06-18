# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from group.models import Group

# Create your views here.

def index(request):
    group_list = Group.objects.all()
    return render(request, 'group/index.html', {'group_list' : group_list})

def detail(request, group_number):
    try:
        group = Group.objects.get(number=group_number)
    except Group.DoesNotExist:
        raise Http404
    return render(request, 'group/detail.html', {'group' : group})
