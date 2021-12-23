from typing import List
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import manager
from django.db.models.fields import NullBooleanField
from django.db.models.query import QuerySet
from django.forms.formsets import formset_factory
from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse ,Http404
from users.models import Manager,Teacher,Student,MassegeT, Attendance,Massege_Student_FromManager,Massege_Student_FromTeacher,Homework,quiz
from homepage import views
from datetime import datetime,timedelta,date
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

    for teacher in teachers:
        count_red=0
        count_green=0
        students_in_class = Student.objects.filter(teacher__user_id = teacher.user_id)
        for j in students_in_class:
            if j.status == False:
                count_red = count_red+1
            elif j.status == True:
                count_green=count_green+1
        teacher.count_red = count_red
        teacher.count_green = count_green

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
    check1 = list(Student.objects.filter(user_id = teacher_user_id)) #check if student with this id allready exist
    check2 = list(Teacher.objects.filter(user_id = teacher_user_id)) #check for Teacher
    check3 = list(Manager.objects.filter(user_id = teacher_user_id)) #check for Manager
    if check1 == [] and check2 == [] and check3 == []: #A user with this id doesnt exist
        new_teacher=Teacher(user_id=teacher_user_id,manager=manager)
        new_teacher.save()
        teachers=Teacher.objects.filter(manager=manager) #for the print in the html file
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
    check1 = list(Student.objects.filter(user_id = student_user_id)) #check if student with this id allready exist
    check2 = list(Teacher.objects.filter(user_id = student_user_id)) #check for Teacher
    check3 = list(Manager.objects.filter(user_id = student_user_id)) #check for Manager
    if check1 == [] and check2 == [] and check3 == []: #A user with this id doesnt exist
        manager=Manager.objects.get(teacher=teacher)
        student=Student(user_id=student_user_id,teacher=teacher,manager=manager)
        student.save()
        students=Student.objects.filter(teacher=teacher)
        return render(request,'teacher/add_success.html',{'students' :students, 'teacher':teacher})
    else:
        return render(request,'teacher/cant_add.html',{'ID' : student_user_id , 'teacher' : teacher})
       



#send massege to teacher from manager
def massegeForTeacher(request,user_id):
    manager = Manager.objects.get(user_id = user_id)
    return render(request,'manager/massegeForT.html',{'manager' : manager})

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
        teacher.read = False
        teacher.save()

    return render(request,'manager/DoneM.html',{'manager' :manager })    



#move to page massege to student from manager
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


#massege in teacher from manager
def massegeFromManagerInTeacher(request,user_id):
    teacher = Teacher.objects.get(user_id=user_id)
    masseges = teacher.masseges.all()
    return render(request,'teacher/getMassege.html',{'teacher' :teacher , 'masseges' : masseges}) 



#move to page massege to student from teacher(all the student on the class)
def massegeForStudent_Teacher(request,user_id):
    teacher = Teacher.objects.get(user_id = user_id)
    return render(request,'teacher/massegeForS.html',{'teacher' : teacher})


#massege for all class from teacher
def submitMassegeForStudent_Teacher(request,user_id):
    teacher = Teacher.objects.get(user_id = user_id)
    author = teacher
    content = request.POST['content']
    subject = request.POST['subject']
    date_create = datetime.now()
    massege = Massege_Student_FromTeacher(author = author,content = content,subject = subject,date_create = date_create)
    massege.save()

    for student in Student.objects.filter(teacher = teacher):
        student.massegeFromTeacher.add(massege)
        student.save()

    return render(request,'teacher/DoneT.html',{'teacher' :teacher })    



#all the massege in student (from mananger and teacher)
def massege_InStudent(request,user_id):
    student = Student.objects.get(user_id=user_id)
    masseges_FromManager = student.massegeFromManager.all()
    masseges_FromTeacher = student.massegeFromTeacher.all()
    return render(request,'student/massege.html',{'student' :student , 'masseges_FromManager' : masseges_FromManager , 'masseges_FromTeacher' :masseges_FromTeacher})


#move to page home work for student from teacher
def homework_Teacher(request,user_id):
    teacher = Teacher.objects.get(user_id=user_id)
    return render(request,'teacher/homework.html',{'teacher' :teacher })

#send home work to student from teacher to all class
def submit_homeworkTeacher(request,user_id):
    teacher = Teacher.objects.get(user_id=user_id)
    students = Student.objects.filter(teacher = teacher)
    students = students.filter(status = False)
    book = request.POST['book']
    pages = request.POST['pages']
    remark = request.POST['remark']
    date_ToDone = request.POST['date_ToDone']
    date_create = datetime.now()
    homeW = Homework(book= book ,pages = pages,remark = remark,date_ToDone = date_ToDone,date_create = date_create)
    homeW.save()

    for student in students:
        student.homework.add(homeW)
        student.read_homework = False
        student.save()
    
    return render(request,'teacher/DoneT.html',{'teacher' :teacher })    

#print home work from teacher in student
def homework_Student(request,user_id):
    student = Student.objects.get(user_id=user_id)
    homework = student.homework.all()
    return render(request,'student/homework.html',{'student' :student , 'homework' :homework})
    


def quizManager(request,user_id):
    #need to add
    manager = Manager.objects.get(user_id=user_id)
    return render(request,'manager/quizManager.html',{'manager' :manager})

#attendece ro class
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
                check_attendance = Attendance(student=student, teacher=teacher, date=date,mark_attendance=mark)  # create new Attendance obj
                check_attendance.save()
                if mark == 'Absent':
                    student.absent = student.absent + 1
                    student.save()
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



                
#change the massege from the manager in teacher to read
def changeToRead_Teacher(request,user_id):
    teacher = Teacher.objects.get(user_id=user_id)
    masseges = teacher.masseges.all()
    teacher.read = True
    teacher.save()
    return render(request, 'teacher/getMassege.html', {'teacher': teacher, 'masseges': masseges})


#change the home work from teacher in student to read
def changeToRead_Student_Homework(request,user_id):
    student = Student.objects.get(user_id=user_id)
    homework = student.homework.all()
    student.read_homework = True
    student.save()
    return render(request,'student/homework.html',{'student' :student , 'homework' :homework})




#change the massege from teacher and manager in student to read
def changeToRead_Student_Massege(request,user_id):
    student = Student.objects.get(user_id=user_id)
    masseges_FromManager = student.massegeFromManager.all()
    masseges_FromTeacher = student.massegeFromTeacher.all()
    student.read_massege = True
    student.save()
    return render(request,'student/massege.html',{'student' :student , 'masseges_FromManager' : masseges_FromManager , 'masseges_FromTeacher' :masseges_FromTeacher})


def StuAdministrativePhones(request,user_id): 
    """Students administrative contact page"""
    student = Student.objects.get(user_id=user_id)
    manager = student.manager
    teacher = student.teacher
    teachers = Teacher.objects.filter(manager = manager)
    context = {
        'student' : student,
        'manager' : manager,
        'my_teacher' : teacher,
        'teachers' : teachers
    }
    return render(request,'student/administrativePhones.html',context)


#send link to quiz from manager from re studenst
def submitQuiz(request,user_id):
    manager = Manager.objects.get(user_id=user_id)
    students = Student.objects.filter(manager=manager)
    students = students.filter(status = False)
    link = request.POST['link']
    date_create = datetime.now()   
    Quiz = quiz(link = link,date_create = date_create)
    Quiz.save()
    for student in students:
        student.quiz.add(Quiz)
        student.read_quiz = False
        student.save()

    return render(request,'manager/DoneM.html',{'manager' :manager })    









        #check1 = Attendance.objects.filter(date=today, student=student)
        #check2 = Attendance.objects.filter(date=yesterday, student=student)
        #check3 = Attendance.objects.filter(date=the_day_before_yesterday, student=student)
        #if check1 and check2 and check3:  # not a quarySet
            #f check1.mark_attendance == 'Absent' and check2.mark_attendance == 'Absent' and check3.mark_attendance == 'Absent' and student.status == False:
             #   lst.append(student.user_id) # all the users id that need to get a quiz

          #today = datetime.today().date().strftime('%d-%m-%Y')
    #yesterday = (date.today() - timedelta(days=1)).strftime('%d-%m-%Y')
    #the_day_before_yesterday = (date.today() - timedelta(days=2)).strftime('%d-%m-%Y')
    #lst = []