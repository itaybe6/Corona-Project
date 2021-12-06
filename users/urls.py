from django.urls import path
from . import views
from django.conf.urls import url

from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('chooseprofile',views.get_chooseprofile, name = 'chooseprofile'),
    path('student/signup',views.get_student_signup, name = 'student_signup'),
    path('teacher/signup',views.get_teacher_signup,name = 'teacher_signup'),
    path(r'manager/signup',views.get_manager_signup, name = 'manager_signup'),
    path(r'manager/signup_success',views.submit_Manager, name = 'submit_Manager'),
    path(r'teacher/signup_success',views.submit_Teacher, name = 'submit_Teacher'),
    path(r'student/signup_success',views.submit_Student, name = 'submit_Student'),
    
    path(r'manager/Home',views.Conect,name = 'Conect'),
    #path(r'teacher/PhonePage',views.PhonesPage , 'PhonesPage'),








]