from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_index(request):
    return HttpResponse('users index')
    #return render(request,'hello.html')


