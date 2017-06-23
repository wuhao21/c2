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
    output = '';
    if request.POST ['choice'] == 'try':
        if request.POST['cipher'] == output:
            res = 'success'
        else:
            res = 'fail'
    else:
        res = 'NONE'
    atk=Attack(attacker=attacker, whom=whom, atype=request.POST['choice'], text=request.POST['text'], key=request.POST['key'], output=output, result=res)
    atk.save()
    return render(request, "attack/detail.html", {'attack' : atk})
