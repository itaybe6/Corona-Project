from django.core.exceptions import ObjectDoesNotExist
from django.db.models import manager
from django.db.models.fields import NullBooleanField
from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse ,Http404
from users.models import Manager,Teacher,Student,MassegeT
from homepage import views
from datetime import datetime


# Create your views here.

def get_student_signup(request):
    return render(request,'student/signup.html')

def get_teacher_signup(request):
    return render(request,'teacher/signup.html')    

def get_manager_signup(request):
    return render(request,'manager/signup.html') 


def submit_Manager(request):
    user_id = request.POST['user_id']
    try: CheckIfManagerExist(user_id)
    except  Manager.DoesNotExist:
        raise Http404(f'Manager with id {user_id} does not exist')
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    school = request.POST['school']
    password = request.POST['password']
    #לשרשום תנאי שאם יש למנהל שאנחנו מנסים לרשום סיסמא אז המנהל רשום ולשלוח לדף של משתמש כבר קיים
    manager = Manager.objects.get(user_id = user_id) 
    manager.name = name
    manager.password = password
    manager.phone_number = phone_number
    manager.school=school
    manager.save()
    return render(request,'manager/signup_success.html') 

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
    teacher = Teacher.objects.get(user_id = user_id)
    teacher.manager = manager
    teacher.name = name
    teacher.password = password
    teacher.user_id = user_id
    teacher.phone_number = phone_number
    teacher.my_class = my_class
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
    student = Student.objects.get(user_id = user_id)
    student.name = name
    student.password = password
    student.user_id = user_id
    student.phone_number = phone_number
    student.teacher=teacher
    student.manager=manager
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
       manager = Manager.objects.get(user_id = user_id)
       teachers = Teacher.objects.filter(manager__user_id = user_id)
       return render(request,'manager/Home.html',{'manager':manager ,'teachers' :teachers})
       
    elif Conect_Stu(user_id,password):
        student = Student.objects.get(user_id = user_id)
        return render(request,'student/Home.html',{'student':student})
        
    elif Conect_Tec(user_id,password):
        teacher = Teacher.objects.get(user_id=user_id)
        return render(request,'teacher/Home.html',{'teacher':teacher})
        
    else:
        return render(request,'ConnectError.html') # אותו דף בית רק עם הודעה של סיסמא שגויה - להוסיף קישור לדף התחברות עם סיסמא שגוייה 
    
    
#Phones page for teacher
def Phones(request,user_id): 
    teacher = Teacher.objects.get(user_id=user_id)
    student = Student.objects.filter(teacher__user_id = user_id)
    return render(request,'teacher/Phones.html' ,{'teacher':teacher, 'student':student})

#Phones page for manager
def PhonesTeacher(request,user_id): 
    manager = Manager.objects.get(user_id=user_id)
    teacher = Teacher.objects.filter(manager__user_id = user_id)
    return render(request,'manager/PhonesT.html', {'manager' : manager , 'teacher' : teacher})

#Phones page for Student
def PhonesStudent(request,user_id):
    student = Student.objects.get(user_id = user_id)
    Students = Student.objects.filter(teacher__user_id = student.teacher.user_id) #list of Student with same teacher
    return render(request,'student/PhoneStu.html', {'Students' : Students , 'student' : student }) # send to func list of studnet and the student 


# 3 functions for path on the site
def HomePageBetweenPathTeacher(request,user_id):
    teacher = Teacher.objects.get(user_id = user_id)
    return render(request,'teacher/Home.html', {'teacher' : teacher})

def HomePageBetweenPathManager(request,user_id):
    manager = Manager.objects.get(user_id=user_id)
    teachers = Teacher.objects.filter(manager__user_id = user_id)
    return render(request,'manager/Home.html',{'manager' :manager ,'teachers' : teachers})

def HomePageBetweenPathStudent(request,user_id):
    student = Student.objects.get(user_id=user_id)
    return render(request,'student/Home.html',{'student' :student})

#שינוי סטטוס של תלמיד לפי הצהרת בריאות
def ChanageStatusStudent(request,user_id):
    student = Student.objects.get(user_id = user_id)
    if(student.status == True):
        student.status = False
        student.save()
    elif(student.status == False):
        student.status = True
        student.save()
    return render(request,'student/changeDoneS.html',{'student' :student})

def ChanageStatusTeacher(request,user_id):
    teacher = Teacher.objects.get(user_id = user_id)
    if(teacher.status == True):
        teacher.status = False
        teacher.save()
    elif(teacher.status == False):
        teacher.status = True
        teacher.save()
    return render(request,'teacher/DoneT.html',{'teacher' :teacher})

def ChanageStatusManager(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    if(manager.status == True):
        manager.status = False
        manager.save()
    elif(manager.status == False):
        manager.status = True
        manager.save()
    return render(request,'manager/DoneM.html',{'manager' :manager})




#graph of status student for manager
def graphStudentStatus(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    teachers = Teacher.objects.filter(manager__user_id = user_id)
    students = Student.objects.filter(manager__user_id = user_id)
    return render(request,'manager/graphStudents.html',{'manager' :manager ,'students' : students ,'teachers' :teachers})


#change all the status of students in class to red
def changeMyClassToRed(request,user_id):
    teacher = Teacher.objects.get(user_id = user_id)
    students = Student.objects.filter(teacher__user_id = user_id)
    for i in students:
        i.status = False
        i.save()
    return render(request,'teacher/Home.html',{'teacher' :teacher})


#manager add teachers
def addTeacher(request,user_id):
    manager=Manager.objects.get(user_id = user_id)
    return render(request,'manager/addTeacher.html',{'manager' : manager})

def submitAddTeacher(request,user_id):
    teacher_user_id = request.POST['teach_user_id']
    manager=Manager.objects.get(user_id = user_id)
    new_teacher=Teacher(user_id=teacher_user_id,manager=manager)
    new_teacher.save()
    teachers=Teacher.objects.all() #for the print in the html file
    return render(request,'manager/add_success.html',{'manager' :manager, 'teachers':teachers})



#manager add new student
def addStudent(request,user_id):
    teacher=Teacher.objects.get(user_id = user_id)
    return render(request,'teacher/addStudent.html',{'teacher' : teacher})


def submitAddStudent(request,user_id):
    student_user_id = request.POST['stu_user_id']
    teacher=Teacher.objects.get(user_id = user_id)
    manager=Manager.objects.get(teacher=teacher)
    student=Student(user_id=student_user_id,teacher=teacher,manager=manager)
    student.save()
    students=Student.objects.all()
    return render(request,'teacher/add_success.html',{'students' :students, 'teacher':teacher})



#send massege to teacher from studnet
def massegeForTeacher(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    return render(request,'manager/massegeForT.html',{'manager' : manager})


#send massege to teacher from studnet
def submitMassegeForTeacher(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    author = manager
    content = request.POST['content']
    subject = request.POST['subject']
    date_create = datetime.now()
    massege = MassegeT(author = author,content = content,subject = subject,date_create = date_create)
    massege.save()

    for teacher in Teacher.objects.all():
        teacher.masseges.add(massege)
        teacher.save()

    return render(request,'manager/DoneM.html',{'manager' :manager }) #להוסיף הודעה נשלחה בהצלחה



#massege in teacher
def massegeFromManagerInTeacher(request,user_id):
    teacher = Teacher.objects.get(user_id=user_id)
    masseges = teacher.masseges.all()
    return render(request,'teacher/getMassege.html',{'teacher' :teacher , 'masseges' : masseges}) 


def quizManager(request,user_id):
    #need to add
    manager = Manager.objects.get(user_id=user_id)
    return render(request,'manager/quizManager.html',{'manager' :manager})