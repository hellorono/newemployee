from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from empweb.models import Departmentmaster,SubDepartmentmaster,EmployeeMaster


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


class DepartmentMasterForm(forms.ModelForm):
    class Meta:
        model=Departmentmaster
        fields=["department_id","department_name","description","created_by_date"]

        widgets={
            "department_id":forms.TextInput(attrs={"class":"form-control"}),
            "department_name":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "created_by_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
 
        }

class SubdepartmentMasterForm(forms.ModelForm):
    class Meta:
        model=SubDepartmentmaster
        fields=["department_id","sub_department_id","sub_department_name","description","created_by_date"]

        widgets={
            "sub_department_id":forms.TextInput(attrs={"class":"form-control"}),
            "department_id":forms.Select(attrs={"class":"form-control"}),
            "sub_department_name":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "created_by_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            
        }

class EmpolyeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeMaster
        fields=["emp_id","name","join_date","department","sub_department","created_by_date","updated_at","updated_by"]

        widgets={
            "emp_id":forms.TextInput(attrs={"class":"form-control"}),
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "join_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            "department":forms.Select(attrs={"class":"form-control"}),
            "sub_department":forms.Select(attrs={"class":"form-control"}),
            "created_by_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            "updated_at":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            "updated_by":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),

        }


