from django.urls import path
from . import views
from django.conf.urls import url

from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path(r'', views.get_index), # ----/users/
    path('chooseprofile',views.get_chooseprofile, name = 'chooseprofile'),
    path('student/signup',views.get_student_signup, name = 'student_signup'),
    path('teacher/signup',views.get_teacher_signup,name = 'teacher_signup'),
    path('manager/signup',views.get_manager_signup, name = 'manager_signup'),
    path('submitManager',views.signup_manager, name = 'submit_manager')








]