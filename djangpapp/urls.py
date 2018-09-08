"""djangpapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('index/',views.index),
    path('date_time',views.date_time),
    path('show',views.show),
    path('index/',views.variable_condition),
    path('load_basic_index',views.load_basic_index),
    path('emp',views.emp),
    path('File_Upload',views.file_upload),
    path('get',views.getdata),
    path('Form_Model',views.index2),
    path('ssession',views.setsession),
    path('gsession',views.getsession),
    path('scookie',views.setcookie),
    path('gcookie',views.getcookie),
    path('csv',views.getfile_csv),
    path('csv_db',views.getfile_csv_db),
    path('pdf',views.getpdf),
    path('my_func',views.my_func),
]
