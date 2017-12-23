
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['usr'] = ['runfeng','aha','haha']
    return render(request,"index.html",context)