from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def williamson(request):
    return HttpResponse('<h1>Williamson can score 50 in semis</h1>')


def ravindra(request):
    return HttpResponse('<h1>Youngest player</h1>')
