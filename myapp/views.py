from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound
import datetime
from django.views.decorators.http import require_http_methods
from django.template import loader
from myapp.form import StuForm
from myapp.form import StudentForm
from myapp.form import EmployeeForm
from myapp.functions.functions import handle_uploaded_file
from myapp.models import Employee,Student,Person
import django.core.exceptions
from django.core.exceptions import ObjectDoesNotExist
import csv
from reportlab.pdfgen import canvas
# Create your views here.

def hello(request):
    return HttpResponse()

def date_time(request):
    now=datetime.datetime.now()
    html="<html><body><h3>Now time is %s.</h3></body></html>"%now
    return HttpResponse(html) #Rendering the template in HttpResponse

def variable_condition(request):
    a=1
    if a:
        return HttpResponseNotFound('<h1>Page Not Found! Hurray!</h1>')
    else:
        return HttpResponse('<h1> Page was found </h1>') #rendering the template in HttpResponse

def load_basic_index(request):
    template=loader.get_template('basic_index.html') #Getting our template
    return HttpResponse(template.render()) #rendering the template in HttpResponse

def index1(request):
    template=loader.get_template('index.html')#getting our template
    name={'student':'Aditya',
          'team_name':'Robotics',
          'name1':'Shyam',
          'name2':'Ranjeet',
          'name3':'Gnaneswar',
          'x':0,
          'y':1,
          }
    return HttpResponse(template.render(name))

def index2(request):
    stu=StuForm()
    return render(request,"index.html",{'form':stu})

def index(request):
    student=StudentForm()
    return render(request,"index.html",{'form':student})

def my_func(request):
    return render(request,"index.html")

def emp(request):
    if request.method=="GET":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})

def file_upload(request):
    if request.method=='POST':
        student=StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
        else:
            return HttpResponse("<h1>Value Error! Please check the values in fields!</h1>")
    else:
        student=StudentForm()
        return render(request,"index.html",{'form':student})

def getdata(request):
    try:
        data=Student.objects.get(id=1)
    except ObjectDoesNotExist:
        return HttpResponse("<h1>Unable to fetch the records</h1>")
    return HttpResponse(data.email)

def setsession(request):
    request.session['sname']='Aditya'
    request.session['semail']='aditya.surampudi@centillionnetworks.com'
    return HttpResponse("Session is set!")

def getsession(request):
    studentname=request.session['sname']
    studentemail=request.session['semail']
    return HttpResponse(studentname+" "+studentemail);

def setcookie(request):
    response=HttpResponse("Cookie Set")
    response.set_cookie('Team_Name','Robotics')
    return response

def getcookie(request):
    tutorial=request.COOKIES['Team_Name']
    return HttpResponse("aditya.surampudi@:"+tutorial);

def getfile_csv(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment;filename="file.csv"'
    writer=csv.writer(response)
    writer.writerow(['1001','John','Domil','CA'])
    writer.writerow(['1002','Amit','Mukharji','LA','Testing'])
    return response

def getfile_csv_db(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="file.csv'
    employees=Employee.objects.all()
    writer=csv.writer(response)
    for emp in employees:
        writer.writerow([emp.eid,emp.ename,emp.econtact])

def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="file.pdf'
    p=canvas.Canvas(response)
    p.setFont("Times-Roman",55)
    p.drawString(100,700,"Hello, Javapoint")
    p.showPage()
    p.save()
    return response


@require_http_methods(['GET'])
def show(request):
    return HttpResponse('<h1>This is Http GET request. </h1>')

