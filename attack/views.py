# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from attack.models import Attack

# Create your views here.

def detail(request, aid):
    int_aid = int(aid)
    try:
        atk = Attack.objects.get(id=int_aid)
    except Attack.DoesNotExist:
        raise Http404
    return render(request, 'attack/detail.html', {'attack' : atk})
def attack_post(request, attacker, whom):
    ctx ={}
    if request.POST:
        ctx['rlt'] = [attacker, whom, request.POST['key'], request.POST['text'], request.POST['choice']]
    return render(request, "group/detail.html", ctx)
