from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields import NullBooleanField
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

     #manager = Manager.objects.get(user_id = user_id)

def submit_Manager(request):
    user_id = request.POST['user_id']
    try: CheckIfManagerExist(user_id)
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

#teacher = Teacher.objects.get(user_id = user_id)
def submit_Teacher(request):
    user_id = request.POST['user_id']
    try:
        CheckIfTeacherExist(user_id)
    except  Teacher.DoesNotExist:
        raise Http404(f'Teacher with id {user_id} does not exist')
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    password = request.POST['password']
    my_class = request.POST['my_class']
    manager = Teacher.objects.get(user_id= user_id).manager
    Teacher.objects.get(user_id = user_id).delete() #delete the object that we created earlier
    teacher = Teacher(name = name,password = password,user_id = user_id, phone_number = phone_number,my_class=my_class, manager=manager)
    teacher.save()
    return render(request,'teacher/signup_success.html') 

def submit_Student(request):
    user_id = request.POST['user_id']
    try:
        CheckIfStudentExist(user_id)
    except  Student.DoesNotExist:
        raise Http404(f'Student with id {user_id} does not exist')
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    password = request.POST['password']
    manager = Student.objects.get(user_id= user_id).manager
    teacher = Student.objects.get(user_id= user_id).teacher
    Student.objects.get(user_id = user_id).delete() #delete the object that we created earlier
    student = Student(name = name,password = password,user_id = user_id, phone_number = phone_number,teacher=teacher, manager=manager)
    student.save()
    return render(request,'student/signup_success.html')     

def get_chooseprofile(request):
    return render(request,'chooseprofile.html')


def CheckIfManagerExist(user_id):

    for i in Manager.objects.all():
        if i.user_id == user_id :
            return True

    return False
            
    


def CheckIfTeacherExist(user_id):
    
    for i in Teacher.objects.all():
        if i.user_id == user_id :
            return True
    return False
            

def CheckIfStudentExist(user_id):

    for i in Student.objects.all():
        if i.user_id == user_id :
            return True
    return False



def Conect_Man(user_id,password):  #Checks the username and password of an managerr
    for i in Manager.objects.all():
        if i.user_id == user_id and i.password == password:
           return True
    return False


def Conect_Tec(user_id,password):  #Checks the username and password of an Teacher
    for i in Teacher.objects.all():
        if i.user_id == user_id and i.password == password:
           return True
    return False

def Conect_Stu(user_id,password):  #Checks the username and password of an Student
    for i in Student.objects.all():
        if i.user_id == user_id and i.password == password:
           return True
    return False


def Conect(request):
    user_id = request.POST['user_id']
    password = request.POST['password']

    if Conect_Man(user_id,password):             # Chack all the users
       return render(request,'manager/Home.html')
       
    elif Conect_Stu(user_id,password):
        return render(request,'student/Home.html')
        
    elif Conect_Tec(user_id,password):
        return render(request,'teacher/Home.html')
        
    else:
        return render(request,'Home/ConnectError.html') # אותו דף בית רק עם הודעה של סיסמא שגויה - להוסיף קישור לדף התחברות עם סיסמא שגוייה 
    
    
def get_student_by_id(request,user_id):
    try:
        student=Student.objects.get(user_id=user_id)
    except Student.DoesNotExist:
        raise Http404('לא קיים סטודנט עם תעודת זהות {user_id}')
    return render(request,'student/Home.html', {'student':student})     






#<form action="logo.php" method="post"> - :הורדתי מהדף של ההתחברות צריך להוסיף כדי לסדר את העיצובex
