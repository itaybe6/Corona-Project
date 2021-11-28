from django.urls import path
from . import views
from django.conf.urls import url


appname = 'users'

urlpatterns = [
    path(r'', views.get_index), # ----/users/
    path('manager/sign-up',views.signup_manager, name = 'sign-up-manager'),
    path('chooseprofile',views.get_chooseprofile, name = 'chooseprofile'),


]