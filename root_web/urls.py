"""root_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

app_name='root'
urlpatterns = [
    #urls of admin site
    path('admin/', admin.site.urls),
    # root url points to the view that opens when there is nothing open
    path('',views.index,name='index'),
    # include the urls of supporters , when 'supp/' us encountered in url django goes to urls in supporter app
    path('supp/',include('supporters.urls')),
      # include the urls of donations , when 'don/' us encountered in url django goes to urls in donations app
    path('don/',include('donation.urls')),
      # include the urls of expenditure , when 'exp/' us encountered in url django goes to urls in expenditure app
    path('exp/',include('exptemp.urls')),
      # include the urls of usersreg , when 'user/' us encountered in url django goes to urls in usersreg app
    path('user/',include('usersreg.urls'))
]
