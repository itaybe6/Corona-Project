from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_homePage(request):
    return render(request,'index.html') #use html file
    