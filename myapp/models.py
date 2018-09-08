from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=20,default="NUll")
    ename=models.CharField(max_length=100,default="NUll")
    econtact =models.CharField(max_length=15,default="NULL")
    #eid = models.IntegerField()
    # class Meta:
    #     db_table="myapp_employee"

class Student(models.Model):
    first_name=models.CharField(max_length=20,default="NUll")
    last_name=models.CharField(max_length=30,default="NUll")
    contact=models.IntegerField()
    email=models.EmailField(max_length=50,default="NUll")
    age=models.IntegerField()
    # class Meta:
    #     db_table="myapp_student"

class Person(models.Model):
    Pname=models.CharField(max_length=20,default="NULL")
    Pid=models.IntegerField()
