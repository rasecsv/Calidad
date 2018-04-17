# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import User

# Create your views here.
from django.http import HttpResponse
from . models import User

def index(request):
	user = User.objects.all()
	return HttpResponse(user)