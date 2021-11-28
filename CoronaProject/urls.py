
import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from CoronaProject import views

urlpatterns = [
    
    url(r'^', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('users/',include('users.urls')),
    path('homepage/',include('homepage.urls')),



]
