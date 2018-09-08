from django import forms
from myapp.models import Student,Employee

class StuForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"