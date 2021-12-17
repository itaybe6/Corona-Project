from django.urls import path
from . import views

app_name= 'homepage'

urlpatterns = [
    path(r'', views.get_homePage, name='home'), # ----/homepage/
    

]