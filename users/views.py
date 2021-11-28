from django.shortcuts import render,redirect
from django.http import HttpResponse ,Http404
from users.models import Manager,Teacher,Student
from homepage import views


from django.contrib.auth import login, authenticate
from django.contrib import messages



# Create your views here.

def get_index(request):
    return HttpResponse('users index')
    #return render(request,'hello.html')

def get_student_signup(request):
    return render(request,'student/signup.html')

def get_teacher_signup(request):
    return render(request,'teacher/signup.html')    

def get_manager_signup(request):
    return render(request,'manager/signup.html') 

def signup_manager(request):
    user_id = request.Post['user_id']
    try :
        manager = Manager.objects.get(user_id = user_id) 
    except Manager.DoesNotExist:
        raise Http404('מנהל לא קיים במערכת. אנא פנה למנהל המערכת')
    name = request.Post['name']
    phone_number = request.Post['phone_number']
    school = request.Post['school']
    password = request.Post['psw']
    
    Manager.objects.get(user_id = user_id).delete() #delete the object that we created earlier
    manager = Manager(name = name,password = password,user_id = ID, phone_number = phone_num,school=school)
    manager.save()
    return render(request,'homepage/index.html',{'users': users})



def get_chooseprofile(request):
    return render(request,'chooseprofile.html')


