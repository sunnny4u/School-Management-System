"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from .views import home,information, check_number,blog_func, con_func



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    #path('',index),
    path('info/<district>',information),
    path('even-odd/<int:number>',check_number),
    path('blog',blog_func),
    path('contact/<name>',con_func),
    path('student/', include('student.urls') )
]
