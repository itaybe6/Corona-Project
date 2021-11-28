from django.shortcuts import render
from django.http import HttpResponse
from users.models import Manager,Teacher,Student
# Create your views here.

def get_index(request):
    return HttpResponse('users index')
    #return render(request,'hello.html')

def log_in_manager(request):
    name = request.Post['name']
    ID = request.Post['userName']
    password = request.Post['password']
    phone_num = request.Post['phone_number']
    school = request.Post['school']

    manager = Manager(name = name,password = password,user_id = ID, phone_number = phone_num,school=school)
    manager.save()
    