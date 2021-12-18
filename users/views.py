from typing import List
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import manager
from django.db.models.fields import NullBooleanField
from django.db.models.query import QuerySet
from django.forms.formsets import formset_factory
from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse ,Http404
from users.models import Manager,Teacher,Student,MassegeT, Attendance,Massege_Student_FromManager
from homepage import views
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import AttendanceForm


# Create your views here.

def get_student_signup(request):
    return render(request,'student/signup.html')

def get_teacher_signup(request):
    return render(request,'teacher/signup.html')    

def get_manager_signup(request):
    return render(request,'manager/signup.html') 

def logout_user(request):
    logout(request)
    return redirect('/')

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
#@login_required
def Phones(request,user_id): 
    teacher = Teacher.objects.get(user_id=user_id)
    student = Student.objects.filter(teacher__user_id = user_id)
    return render(request,'teacher/Phones.html' ,{'teacher':teacher, 'student':student})

#Phones page for manager
#@login_required
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
    return render(request,'teacher/DoneT.html',{'teacher' :teacher})


#manager add teachers
def addTeacher(request,user_id):
    manager=Manager.objects.get(user_id = user_id)
    return render(request,'manager/addTeacher.html',{'manager' : manager})

def submitAddTeacher(request,user_id):
    teacher_user_id = request.POST['teach_user_id']
    manager=Manager.objects.get(user_id = user_id)
    if list(Teacher.objects.filter(user_id = teacher_user_id)) == []: #A teacher with this id doesnt exist
        new_teacher=Teacher(user_id=teacher_user_id,manager=manager)
        new_teacher.save()
        teachers=Teacher.objects.all() #for the print in the html file
        return render(request,'manager/add_success.html',{'manager' :manager, 'teachers':teachers})    
    else:
        return render(request,'manager/cant_add.html',{'ID' : teacher_user_id , 'manager' : manager})



#manager add new student
def addStudent(request,user_id):
    teacher=Teacher.objects.get(user_id = user_id)
    return render(request,'teacher/addStudent.html',{'teacher' : teacher})


def submitAddStudent(request,user_id):
    student_user_id = request.POST['stu_user_id']
    teacher=Teacher.objects.get(user_id = user_id)
    check = list(Student.objects.filter(user_id = student_user_id)) #check if student with this id allready exist
    if check == []: #A student with this id doesnt exist
        manager=Manager.objects.get(teacher=teacher)
        student=Student(user_id=student_user_id,teacher=teacher,manager=manager)
        student.save()
        students=Student.objects.all()
        return render(request,'teacher/add_success.html',{'students' :students, 'teacher':teacher})
    else:
        return render(request,'teacher/cant_add.html',{'ID' : student_user_id , 'teacher' : teacher})
       



#send massege to teacher from manager
def massegeForTeacher(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    return render(request,'manager/massegeForT.html',{'manager' : manager})

#send massege to teacher from Manager
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

    return render(request,'manager/DoneM.html',{'manager' :manager })    



#send massege to student from manager
def massegeForStudent_Manager(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    return render(request,'manager/massegeForS.html',{'manager' : manager})

#send massege to student from manager
def submitMassegeForStudent_Manager(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    author = manager
    content = request.POST['content']
    subject = request.POST['subject']
    date_create = datetime.now()
    massege = Massege_Student_FromManager(author = author,content = content,subject = subject,date_create = date_create)
    massege.save()

    for student in Student.objects.all():
        student.massegeFromManager.add(massege)
        student.save()

    return render(request,'manager/DoneM.html',{'manager' :manager })    


#massege in teacher
def massegeFromManagerInTeacher(request,user_id):
    teacher = Teacher.objects.get(user_id=user_id)
    masseges = teacher.masseges.all()
    return render(request,'teacher/getMassege.html',{'teacher' :teacher , 'masseges' : masseges}) 


def massegeFromManagerInStudent(request,user_id):
    student = Student.objects.get(user_id=user_id)
    masseges = student.massegeFromManager.all()
    return render(request,'student/masFromMan.html',{'student' :student , 'masseges' : masseges})


def quizManager(request,user_id):
    #need to add
    manager = Manager.objects.get(user_id=user_id)
    return render(request,'manager/quizManager.html',{'manager' :manager})

def mark_attendance(request,user_id):
    teacher = Teacher.objects.get(user_id=user_id)
    students = Student.objects.filter(teacher=teacher)
    count = students.count() #how many students
    attendance_formset = formset_factory(AttendanceForm, extra=count)
    date = datetime.today().date().strftime('%d-%m-%Y')
    attendance = None

    if request.method == 'POST':
        formset = attendance_formset(request.POST)
        lst = zip(formset,students)

        if formset.is_valid(): #for cleaned_data func
            for form, student in zip(formset,students): #form->formset, student->students
                date = datetime.today()
                mark = form.cleaned_data['mark_attendance'] 
                check_attendance = Attendance.objects.filter(teacher=teacher,date=date,student=student) #if checked
                if check_attendance:
                    attendance = Attendance.objects.get(student=student,teacher=teacher,date=date)
                    if attendance.mark_attendance == 'Absent':
                        student.absent = student.absent - 1
                    elif attendance.mark_attendance == 'Present':
                        student.present = student.present - 1
                    attendance.mark_attendance = mark
                    attendance.save()
                else:  #if not check (check_attendance is QuarySet)->The student acsent and present wont change
                    check_attendance = Attendance()
                    check_attendance.teacher = teacher
                    check_attendance.student = student
                    check_attendance.date = date
                    check_attendance.mark_attendance = mark
                    check_attendance.save()

                if mark == 'Absent':
                    student.absent = student.absent + 1
                if mark == 'Present':
                    student.present = student.present + 1
                student.save()


            context = {
                'students': students,
                'teacher': teacher,
            }
            return render(request, 'teacher/attendance_success.html', context) #attendance suuccess
        else: #formset is not vaid->something went wrong (need to do the attendance again)
            context = {
                'formset': formset,
                'students': students,
                'teacher': teacher,
                'list': lst,
                'date':date,
            }
            return render(request, 'teacher/attendance_form.html', context)

    else: #the user want to start the attendance check (when press the attendance bottum)
        lst = zip(students, attendance_formset())
        context = {
            'formset': attendance_formset(),
            'students': students,
            'teacher': teacher,
            'list': lst,
            'date':date,
        }

        return render(request, 'teacher/attendance_form.html', context)

