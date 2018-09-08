from django import forms
from myapp.models import Student,Employee
from djangpapp import settings
class StuForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class StudentForm(forms.Form):
    firstname=forms.CharField(label="Enter first name:",max_length=50)
    lastname=forms.CharField(label="Enter last name:",max_length=100)
    gender=forms.BooleanField(label="Enter your gender:")
    #course=forms.ChoiceField(label="Enter the Course details:")
    my_date=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,label="Enter the date")
    #my_date_time=forms.DateTimeField(label="Enter the date & time")
    marks=forms.DecimalField(label="Enter the marks obtained")
    email=forms.EmailField(label="Enter the Email Id:")
    file=forms.FileField()
    #my_image=forms.ImageField(label="Enter the Image:")

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class StudentForm1(forms.Form):
    firstname=forms.CharField(label="Enter first name",max_length=50)
    lastname=forms.CharField(label="Enter last name",max_length=10)
    email=forms.EmailField(label="Enter Email")
    file=forms.FileField()#for creating file input
