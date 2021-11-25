from django.urls import path
from . import views
#from users import views
#from django.conf.urls import url


urlpatterns = [
    path(r'', views.get_index), # ----/users/
    path('name/', views.get_name),# ----/users/name/

]