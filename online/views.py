# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from online.models import User
f = open('indexmd.txt')
content = f.read()

class UserForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
#get info from userform
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
#comparison
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                req.session['onlineuser'] = username
                return render(req, 'index.html' , {'content': content, 'status': 'in', 'username': username})
            else:
                return render(req, 'index.html' , {'content': content, 'status': 'wrong', 'username':''})
    else:
        uf = UserForm()
    return render_to_response('online/login.html',{'uf':uf})

def logout(req):
    try:
        del req.session['who']
    except KeyError:
        pass
    return render(req, 'index.html' , {'content': content, 'status': 'out', 'username':''})
