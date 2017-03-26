# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Candidate

# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request,'elections/index.html', context)

def areas(request, area):
    return HttpResponse(area)