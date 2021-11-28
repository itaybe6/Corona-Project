from django.urls import path
#from .viwes import NAME_FUNCTIONS....
from django.conf.urls import url

app name = 'user'

urlpatterns = [
    path(r'', views.get_index), # ----/users/
    path('manager/login.html',log_in_manager,name ='login-manager')


]