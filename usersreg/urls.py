from django.urls import path
from . import views

app_name = 'usersreg'

urlpatterns = [
    path('login/',views.loginu,name='login'),
    path('logout/',views.logoutu,name='logout'),
    path('index/',views.index, name = 'index'),
    path('addmem/',views.add_mem,name='add_mem')
]