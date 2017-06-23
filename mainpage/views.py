# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from mainpage.models import MainPage

# Create your views here.

def index(request):
    try :
        index = MainPage.objects.get(title = 'SU2016')
    except MainPage.DoesNotExist:
        raise Http404
    return render(request, 'mainpage/index.html', {'page' : index, 'status' : 'new', 'username': ''})

