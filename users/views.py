from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse ,Http404
from users.models import Manager,Teacher,Student
from homepage import views


# Create your views here.

def get_student_signup(request):
    return render(request,'student/signup.html')

def get_teacher_signup(request):
    return render(request,'teacher/signup.html')    

def get_manager_signup(request):
    return render(request,'manager/signup.html') 

def submit_Manager(request):
    user_id = request.POST['user_id']
    try:
         manager = Manager.objects.get(user_id = user_id)
    except  Manager.DoesNotExist:
        raise Http404(f'Manager with id {user_id} does not exist')
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    school = request.POST['school']
    password = request.POST['password']
    Manager.objects.get(user_id = user_id).delete() #delete the object that we created earlier
    manager = Manager(name = name,password = password,user_id = user_id, phone_number = phone_number,school=school)
    manager.save()
    return render(request,'manager/signup_success.html') 

def submit_Teacher(request):
    user_id = request.POST['user_id']
    try:
         teacher = Teacher.objects.get(user_id = user_id)
    except  Teacher.DoesNotExist:
        raise Http404(f'Teacher with id {user_id} does not exist')
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    password = request.POST['password']
    my_class = request.POST['my_class']
    manager = Teacher.objects.get(user_id= 126).manager
    Teacher.objects.get(user_id = user_id).delete() #delete the object that we created earlier
    teacher = Teacher(name = name,password = password,user_id = user_id, phone_number = phone_number,my_class=my_class, manager=manager)
    teacher.save()
    return render(request,'teacher/signup_success.html') 

def get_chooseprofile(request):
    return render(request,'chooseprofile.html')


