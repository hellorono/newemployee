from django.shortcuts import render,redirect
from empweb import models
from django.views.generic import CreateView,FormView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,LoginForm,DepartmentMasterForm,SubDepartmentmaster
from empweb.models import Departmentmaster,SubDepartmentmaster


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
    
class DeptMasterView(CreateView,ListView):
    template_name = 'deptmaster.html'
    form_class = DepartmentMasterForm
    model = Departmentmaster
    success_url = reverse_lazy('index')
    queryset=Departmentmaster.objects.all()
    context_object_name="deptmaster"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class SubdeptmasterView(CreateView,ListView):
    template_name = 'Subdeptmaster.html'
    form_class = DepartmentMasterForm
    model = SubDepartmentmaster
    success_url = reverse_lazy('index')
    queryset=Departmentmaster.objects.all()
    context_object_name="subdeptmaster"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



    
    
    

   


