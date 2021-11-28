from django.urls import path
from . import views
from django.conf.urls import url


appname = 'users'

urlpatterns = [
    path(r'', views.get_index), # ----/users/
    path('chooseprofile',views.get_chooseprofile, name = 'chooseprofile'),
    path('student/signup',views.get_student_signup, name = 'student_signup'),
    path('teacher/signup',views.get_teacher_signup,name = 'teacher_signup'),
    path('manager/signup',views.get_manager_signup, name = 'manager_signup'),






]