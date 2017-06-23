# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from attack.models import Attack
import os
f = open('indexmd.txt')
content = f.read()

# Create your views here.

def detail(request, aid):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    int_aid = int(aid)
    try:
        atk = Attack.objects.get(id=int_aid)
    except Attack.DoesNotExist:
        raise Http404
    return render(request, 'attack/detail.html', {'attack' : atk, 'username' : username})
def attack_post(request, whom):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    output = '';
    if request.POST ['choice'] == 'try':
        if request.POST['cipher'] == output:
            res = 'success'
        else:
            res = 'fail'
    else:
        res = 'NONE'
    atk=Attack(attacker=request.session['who'], whom=whom, atype=request.POST['choice'], text=request.POST['text'], key=request.POST['key'], output=output, result=res)
    atk.save()
    return render(request, "attack/detail.html", {'attack' : atk, 'username' : username})
