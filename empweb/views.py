from django.shortcuts import render,redirect

from empweb import models
from django.views.generic import CreateView,FormView,ListView,UpdateView,TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from .forms import UserRegistrationForm,LoginForm,DepartmentMasterForm,SubdepartmentMasterForm,EmpolyeeForm
from empweb.models import Departmentmaster,SubDepartmentmaster,EmployeeMaster

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper

decs=[signin_required,never_cache]


class SignUpView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    success_url=reverse_lazy("index")

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render (request,self.template_name,{"form":form})
            


@method_decorator(decs,name="dispatch")
class IndexView(ListView,LoginRequiredMixin):
    template_name="index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

@method_decorator(decs,name="dispatch")
class DeptMasterView(ListView):
    template_name='departmentmaster.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
@method_decorator(decs,name="dispatch")
class DeptMasterCreateView(TemplateView):
    def get(self,request,*args,**kw):
        form=DepartmentMasterForm()
        context={"form":form}
        return render (request,"add_deptmaster.html",context)
    
    def post(self,request,*args,**kw):
        form=DepartmentMasterForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

            return redirect("list-deptmaster")
        else:
            return render(request,"add-deptmaster",{"form":form})

@method_decorator(decs,name="dispatch")
class DeptMasterListView(ListView):
    template_name="list_deptmaster.html"
    model=Departmentmaster
    
    def get(self,request,*args,**kw):
        data=Departmentmaster.objects.all()
        context={'data':data}
        return render(request,'list_deptmaster.html',context)

@method_decorator(decs,name="dispatch")
class UpdateDepartmentMaster(TemplateView):
    def get(self,request,*args,**kw):
        obj=Departmentmaster.objects.get(department_id=kw["pk"])
        form=DepartmentMasterForm(instance=obj)
        context={"form":form}
        return render (request,"updatedepmaster.html",context)
    
    def post(self,request,*args,**kw):
        obj=Departmentmaster.objects.get(department_id=kw["pk"])
        form=DepartmentMasterForm(instance=obj,data=request.POST)
        if form.is_valid():

            instance=form.save(commit=False)
            instance.save()

            return redirect("list-deptmaster")
        else:
            return render(request,"updatedepmaster.html",{"form":form})


def departmentmaster_delete(request,pk):
    if request.method=="GET":
        id=pk
        Departmentmaster.objects.get(department_id=id).delete()
        return redirect("list-deptmaster")

@method_decorator(decs,name="dispatch")
class SubDeptMasterView(ListView):
    template_name='subdeptmaster.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

@method_decorator(decs,name="dispatch")
class SubdeptCreateView(TemplateView):
    def get(self,request,*args,**kw):
        form=SubdepartmentMasterForm()
        context={"form":form}
        return render (request,"add_sub.html",context)

    def post(self,request,*args,**kw):
        form=SubdepartmentMasterForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

            return redirect("list_sub")
        else:
            return render(request,"add_sub",{"form":form})

@method_decorator(decs,name="dispatch")
class SubdeptListView(ListView):
    template_name="list_sub.html"
    model=SubDepartmentmaster

    def get(self,request,*args,**kw):
        data=SubDepartmentmaster.objects.all()
        context={"data":data}
        return render(request,'list_sub.html',context)

@method_decorator(decs,name="dispatch")
class UpdateSubDepartmentMasterView(TemplateView):
    def get(self,request,*args,**kw):
        obj=SubDepartmentmaster.objects.get(sub_department_id=kw["pk"])
        form=SubdepartmentMasterForm(instance=obj)
        context={"form":form}
        return render (request,"update_sub.html",context)
    
    def post(self,request,*args,**kw):
        obj=SubDepartmentmaster.objects.get(sub_department_id=kw["pk"])
        form=SubdepartmentMasterForm(instance=obj,data=request.POST)
        if form.is_valid():
            
            instance=form.save(commit=False)
            instance.save()

            return redirect("list_sub")
        else:
            return render(request,"update_sub.html",{"form":form})
            
def delete_sub(request,pk):
    if request.method=="GET":
        id=pk
        SubDepartmentmaster.objects.get(sub_department_id=id).delete()
        return redirect("list_sub")

@method_decorator(decs,name="dispatch")    
class EmployeeMasterView(ListView):
    template_name="employeemaster.html"
    def get(self,request,*args,**kw):
        return render(request,self.template_name)


@method_decorator(decs,name="dispatch")
class EmployeeCreateView(TemplateView):
    def get(self,request,*args,**kw):
        form=EmpolyeeForm()
        context={"form":form}
        return render(request,"emp_add.html",context)

    def post(self,request,*args,**kw):
        form=EmpolyeeForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect("emp_list")
        else:
            return render(request,"emp_add.html",{"form":form})

@method_decorator(decs,name="dispatch")
class EmployeeListView(ListView):
    template_name="emp_list.html"
    model=EmployeeMaster

    def get(self,request,*args,**kw):
        data=EmployeeMaster.objects.all()
        context={"data":data}
        return render(request,"emp_list.html",context)

@method_decorator(decs,name="dispatch")
class UpdateEmployeeListView(TemplateView):
    def get(self,request,*args,**kw):
        obj=EmployeeMaster.objects.get(emp_id=kw["pk"])
        form=EmpolyeeForm(instance=obj)
        context={"form":form}
        return render(request,"emp_update.html",context)

    def post(self,request,*args,**kw):
        obj=EmployeeMaster.objects.get(emp_id=kw["pk"])
        form=EmpolyeeForm(instance=obj,data=request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect("emp_list")
        else:
            return render(request,"emp_update.html",{"form":form})
        
def delete_employee(request,pk):
    if request.method=="GET":
        id=pk
        EmployeeMaster.objects.get(emp_id=id)
        return redirect("emp_list")
    
def sign_out_view(request,*args,**kw):
    logout(request)
    return redirect("signin")


    



    
    

    






    
    
    

   


