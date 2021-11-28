from django.urls import path
from . import views
from django.conf.urls import url


appname = 'user'

urlpatterns = [
    path(r'', views.get_index), # ----/users/
    path('manager/login',views.log_in_manager)


]