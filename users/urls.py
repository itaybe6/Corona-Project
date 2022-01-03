from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'users'

urlpatterns = [
    url(r'^logout/$', views.logout_user, name='logout_user'),
    path('chooseprofile',views.get_chooseprofile, name = 'chooseprofile'),

    #move to register page 
    path('student/signup',views.get_student_signup, name = 'student_signup'),
    path('teacher/signup',views.get_teacher_signup,name = 'teacher_signup'),
    path(r'manager/signup',views.get_manager_signup, name = 'manager_signup'),

    #register for manager,teacher and student
    path(r'manager/signup_success',views.submit_Manager, name = 'submit_Manager'),
    path(r'teacher/signup_success',views.submit_Teacher, name = 'submit_Teacher'),
    path(r'student/signup_success',views.submit_Student, name = 'submit_Student'),
    
    #connect to all the users
    path(r'Home',views.Conect,name = 'Conect'),

    #phone pages in manager teacher and student
    path('Phones/897<int:user_id>654/',views.Phones),
    path('PhonesT/897<int:user_id>654',views.PhonesTeacher,name = 'PhonesT'),
    path('PhoneStu/897<int:user_id>654',views.PhonesStudent, name = 'PhoneStu'),
    path('StuAdministrativePhones/897<int:user_id>654',views.StuAdministrativePhones, name = 'StuAdministrativePhones'),


    #Home page between paths on the site
    path(r'HomePageTeacher/897<int:user_id>654/',views.HomePageBetweenPathTeacher,name = 'HomePageTeacher'),
    path(r'HomePageManager/897<int:user_id>654/',views.HomePageBetweenPathManager,name = 'HomePageManager'),
    path(r'HomePageStudent/897<int:user_id>654/',views.HomePageBetweenPathStudent, name = 'HomePageStudent'),

    #change status in all the users
    path('ChanageStatusStudent/897<int:user_id>654/',views.ChanageStatusStudent , name = 'ChanageStatusStudent'),
    path('ChanageStatusTeacher/897<int:user_id>654/',views.ChanageStatusTeacher , name = 'ChanageStatusTeacher'),
    path('ChanageStatusManager/897<int:user_id>654/',views.ChanageStatusManager , name = 'ChanageStatusManager'),

    #graph of student status in manager
    path('graphStudentStatus/897<int:user_id>654/',views.graphStudentStatus, name = 'graphStudentStatus'),

    #change all the status of students in class to red
    path('changeMyClassToRed/897<int:user_id>654/',views.changeMyClassToRed,name = 'changeMyClassToRed'),

    #send massege to teacher from manager
    path('massegeForTeacher/897<int:user_id>654/',views.massegeForTeacher, name ='massegeForTeacher'), 
    path('submitMassegeForTeacher/897<int:user_id>654/',views.submitMassegeForTeacher,name = 'submitMassegeForTeacher'),
    
    #send massege to student from manager
    path('massegeForStudentManager/897<int:user_id>654/',views.massegeForStudent_Manager,name = 'massegeForStudentManager' ),
    path('submitMassegeForStudent_Manager/897<int:user_id>654/',views.submitMassegeForStudent_Manager , name = 'submitMassegeForStudent_Manager' ),

    #send massege to class from teacher
    path('massegeForStudentTeacher/897<int:user_id>654/',views.massegeForStudent_Teacher,name='massegeForStudentTeacher'),
    path('submitMassegeForStudent_Teacher/897<int:user_id>654/',views.submitMassegeForStudent_Teacher,name= 'submitMassegeForStudent_Teacher'),

    #get massege from manager in teacher
    path('massegesFromManagerInTeacher/897<int:user_id>654/',views.massegeFromManagerInTeacher, name='massegeFromManagerInTeacher'),

    #get massege from teacher and mangager in student
    path('massege_InStudent/897<int:user_id>654/',views.massege_InStudent,name = 'massege_InStudent'),


    #send home work to student from teacher
    path('homework_Teacher/897<int:user_id>654/',views.homework_Teacher,name='homework_Teacher'),
    path('submit_homeworkTeacher/897<int:user_id>654/' ,views.submit_homeworkTeacher,name = 'submit_homeworkTeacher'),

    #get home work from teacher in student
    path('homework_Student/897<int:user_id>654/',views.homework_Student,name = 'homework_Student'),

    #change the massege from the manager in teacher to read
    path('changeToRead_Teacher/897<int:user_id>654/',views.changeToRead_Teacher,name = 'changeToRead_Teacher'),
    
    #change the homework from teacher in student to read
    path('changeToRead_Student_Homework/897<int:user_id>654/',views.changeToRead_Student_Homework, name = 'changeToRead_Student_Homework'),
    
    #change the massege from teacher and manager in student to read
    path('changeToRead_Student_Massege/897<int:user_id>654/',views.changeToRead_Student_Massege, name = "changeToRead_Student_Massege"),

    #add student in teacher 
    path('addStudent/<int:user_id>/',views.addStudent, name = 'addStudent'),
    path('submitAddStudent/<int:user_id>/',views.submitAddStudent, name = 'submitAddStudent'),

    #add teacher in manager
    path('addTeacher/<int:user_id>/',views.addTeacher, name = 'addTeacher'),
    path('submitAddTeacher/<int:user_id>/',views.submitAddTeacher, name = 'submitAddTeacher'),

    #quiz to student in manager
    path('quizManager/<int:user_id>/',views.quizManager, name = 'quizManager'),
    path('submitQuiz/<int:user_id>/',views.submitQuiz, name = 'submitQuiz' ),

    #quiz from manager in student
    path('quizStudent/897<int:user_id>654/',views.quizStudent, name = 'quizStudent'),
    path('answerQuiz/897<int:user_id>654/',views.answerQuiz, name = 'answerQuiz'),


    path('mark_attendance/<int:user_id>/',views.mark_attendance, name='mark_attendance'),

    #guide of the site in studnet
    path('guideToStudent/897<int:user_id>654/',views.guideToStudent,name ='guideToStudent'),


]
urlpatterns += staticfiles_urlpatterns()