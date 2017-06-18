# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from attack.models import Attack

# Create your views here.

def detail(request, aid):
    try:
        atk = Attack.objects.get(id=aid)
    except Attack.DoesNotExist:
        raise Http404
    return render(request, 'attack/detail.html', {'attack' : atk})
