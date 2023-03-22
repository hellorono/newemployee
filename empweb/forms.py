from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from empweb.models import Departmentmaster,SubDepartmentmaster


class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class DepartmentMasterForm(forms.Form):
    class Meta:
        model=Departmentmaster
        fields=["department_id","department_name","description","created_by_date","created_at_date"]

        widgets={
            "department_id":forms.TextInput(attrs={"class":"form-control"}),
            "department_name":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "created_by_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            "created_at_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
        }

class SubdepartmentMasterForm(forms.Form):
    class Meta:
        model=SubDepartmentmaster
        fields=["sub_department_id","department_name","description","created_by_date","created_at_date"]

        widgets={
            "sub_department_id":forms.TextInput(attrs={"class":"form-control"}),
            "department_id":forms.TextInput(attrs={"class":"form-control"}),
            "sub_department_name":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "created_by_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            "created_at_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
        }



