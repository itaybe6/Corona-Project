from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_myname(request):
    #return HttpResponse(' Hello! my name is Rotem ')
    return render(request,'hello.html', {'name': 'Rotem'})


