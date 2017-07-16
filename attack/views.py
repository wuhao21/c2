# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from attack.models import Attack
import os
f = open('indexmd.txt')
content = f.read()
f.close()

# Create your views here.

def list(request):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    return render(request, 'attack/list.html', {'username' : username})

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

    op = request.POST['choice'];
    if op == 'try': op = 'encrypt'
    key = request.POST['key'];
    
    if op == 'decrypt':
    	f = open("data/%s/CIPHER")
    	cipher = f.read()
    	if request.POST['text'] == cipher:
    		return render(request, 'index.html' , {'content': content, 'status': 'wrong', 'username':''})
	
    if key == '':
        temp_file = os.popen("data/%s/c2 --%s \'%s\'"%(whom, op, request.POST['text']))
    else:
        temp_file = os.popen("data/%s/c2 --%s \'%s\' --key \'%s\'"%(whom, op, request.POST['text'], key))
    output = temp_file.read()
    temp_file.close()

    if request.POST ['choice'] == 'try':
        if request.POST['cipher'] == output:
            res = 'success'
        else:
            res = 'fail'
    else:
        res = 'NONE'
    atk=Attack(attacker=request.session['who'], whom=whom, atype=request.POST['choice'], text=request.POST['text'], key=request.POST['key'], output=output, result=res)
    atk.save()
    return render(request, 'attack/detail.html', {'attack' : atk, 'username' : username})

def history(request):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    atklist = Attack.objects.filter(attacker=username)
    return render(request, 'attack/history.html', {'atklist' : atklist, 'username' : username})

