from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return HttpResponse('<h1>Made centurary in semis </h1>')


def shreyas(request):
    return HttpResponse('<h1>Made centurary in worldcup with newzealand</h1>')