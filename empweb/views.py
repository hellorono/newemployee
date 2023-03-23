from django.shortcuts import render,redirect

from empweb import models
from django.views.generic import CreateView,FormView,ListView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,LoginForm,DepartmentMasterForm,SubdepartmentMasterForm,EmpolyeeForm
from empweb.models import Departmentmaster,SubDepartmentmaster,EmployeeMaster


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
            



            
class IndexView(ListView,LoginRequiredMixin):
    template_name="index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    




    
class DeptMasterView(ListView):
    template_name='departmentmaster.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class DeptMasterCreateView(CreateView):
    template_name = 'add_deptmaster.html'
    form_class = DepartmentMasterForm
    model = Departmentmaster

    def post(self,request,*args,**kw):
        form=DepartmentMasterForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

            return redirect("list-deptmaster")
        else:
            return render(request,"add-deptmaster",{"form":form})

class DeptMasterListView(ListView):
    template_name="list_deptmaster.html"
    model=Departmentmaster
    
    def get(self,request,*args,**kw):
        data=Departmentmaster.objects.all()
        context={'data':data}
        return render(request,'list_deptmaster.html',context)

class UpdateDepartmentMaster(UpdateView):
    template_name = 'updatedepmaster.html'
    form_class = DepartmentMasterForm
    model = Departmentmaster
    success_url = reverse_lazy('list-deptmaster')

def departmentmaster_delete(request,pk):
    id=pk
    Departmentmaster.objects.get(department_id=id).delete()
    return redirect("list-deptmaster")


    





class SubDeptMasterView(ListView):
    template_name='subdeptmaster.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SubdeptCreateView(CreateView):
    template_name = 'Subdeptmaster.html'
    form_class = SubdepartmentMasterForm
    model = SubDepartmentmaster

    def post(self,request,*args,**kw):
        form=SubdepartmentMasterForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

            return redirect("list_sub")
        else:
            return render(request,"add_sub",{"form":form})

class SubdeptListView(ListView):
    template_name="list_sub.html"
    model=SubDepartmentmaster

    def get(request,*args,**kw):
        data=SubDepartmentmaster.objects.all()
        context={"data":data}
        return render(request,'list_sub.html',context)

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)
    
    # def form_valid(self, form):
    #     form.instance.user=self.request.user
    #     return super().form_valid(form)
    
class UpdateSubDepartmentMaster(UpdateView):
    template_name = 'updatesubdepmaster.html'
    form_class = SubdepartmentMasterForm
    model = SubDepartmentmaster
    success_url = reverse_lazy('updatesubdepmaster.html')




    
class EmployeeView(CreateView,ListView):
    template_name = 'employee.html'
    form_class = EmpolyeeForm
    model = SubDepartmentmaster
    success_url = reverse_lazy('employee.html')
    queryset=EmployeeMaster.objects.all()
    context_object_name="employee"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class UpdateEmployee(UpdateView):
    template_name = 'updateemployee.html'
    form_class = DepartmentMasterForm
    model = Departmentmaster
    success_url = reverse_lazy('updateemployee.html')

def employee_delete(request,*args,**kw):
    id=kw.get("id")
    EmployeeMaster.objects.get(id=id).delete()
    return redirect("employee.html")
    
    

    






    
    
    

   


