# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from django.shortcuts import render
from attack.models import Attack
from django.http import Http404
import os

from group.models import Group
from login.models import User

f = open('index.md')
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

def attack_cpca(request, whom):
    try:
        username = request.session['who']
        op = request.POST['choice'];
        op = re.sub(r'[^a-zA-Z]', '', op)
        if op == 'try': op = 'encrypt'
        key = request.POST['key'];
        text = request.POST['text'];
        text = re.sub(r'[^a-zA-Z0-9,\.\;\?\!\(\)]', '', text)
        whom = re.sub(r'[^0-9\-]', '', whom)
    except:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    try:
        if key == '':
            temp_file = os.popen("data/%s/c2 --%s \'%s\' -k data/%s/keyfile.txt" % (whom, op, text,whom))
        else:
            temp_keyfile = open("data/%s/tempkey.txt" % (whom), 'w')
            temp_keyfile.write(key)
            temp_keyfile.close()
            temp_file = os.popen(
                "data/%s/c2 --%s \'%s\' --key data/%s/tempkey.txt" % (whom, op, text, whom))
        output = temp_file.read()
        temp_file.close()
        res = 'NONE'
        atk = Attack(attacker=request.session['who'], whom=whom, atype=request.POST['choice'],
                     text=request.POST['text'],
                     key=request.POST['key'], output=output, result=res)
        atk.save()
    except:
        output = 'DecodeError!'
    try:
        group = Group.objects.get(gid=whom)
    except Group.DoesNotExist:
        raise Http404
    return render(request, 'group/detail.html', {'group': group, 'username': username, 'result': output, 'key': ''})

def attack_post(request, whom):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})

    try:
        group = Group.objects.get(gid=whom)
    except Group.DoesNotExist:
        raise Http404

    if group.plaintext == request.POST['plaintext']:
        res = 'success'
        try:
            attacker = User.objects.get(username=username)
            defender = User.objects.get(username=group.username)
        except User.DoesNotExist:
            raise Http404
        attacker.score += group.score*2
        defender.score -= group.score*2
        attacker.save()
        defender.save()
    else:
        res = 'fail'
    atk=Attack(attacker=request.session['who'], whom=whom, atype='try', text='', key='', output='NONE', result=res)
    atk.save()
    return render(request, 'attack/detail.html', {'attack' : atk, 'username' : username})

def history(request):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    atklist = Attack.objects.filter(attacker=username).order_by("-date_time")
    return render(request, 'attack/history.html', {'atklist' : atklist, 'username' : username})

def leaderboard(request):
    try:
        username = request.session['who']
    except KeyError:
        return render(request, 'index.html' , {'content': content, 'status': 'old', 'username':''})
    userlist = User.objects.exclude(username = 'zcccc').order_by("-score")
    return render(request, 'attack/leaderboard.html', {'userlist' : userlist, 'username' : username})

