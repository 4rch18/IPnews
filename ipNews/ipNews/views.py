__author__ = 'hap1521'

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
