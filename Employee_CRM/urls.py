"""Employee_CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from empweb.views import SignInView,SignUpView,IndexView,DeptMasterCreateView,DeptMasterListView,SubDeptMasterView,DeptMasterView,UpdateDepartmentMaster,departmentmaster_delete,SubdeptCreateView,SubdeptListView,UpdateSubDepartmentMasterView,delete_sub,EmployeeMasterView,EmployeeCreateView,EmployeeListView,UpdateEmployeeListView,delete_employee,sign_out_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login",SignInView.as_view(),name="signin"),
    path("",SignUpView.as_view(),name="signup"),
    path("index",IndexView.as_view(),name="index"),
    path("deptmaster",DeptMasterView.as_view(),name="deptmaster"),
    path("add-deptmaster",DeptMasterCreateView.as_view(),name="add-deptmaster"),
    path("list-deptmaster",DeptMasterListView.as_view(),name="list-deptmaster"),
    path("update/<int:pk>",UpdateDepartmentMaster.as_view(),name="update"),
    path("delete/<int:pk>",departmentmaster_delete,name="dep_mas_delete"),

    path("subept",SubDeptMasterView.as_view(),name="subdept"),
    path("add_sub",SubdeptCreateView.as_view(),name="add_sub"),
    path("list_sub",SubdeptListView.as_view(),name="list_sub"),
    path("sub_update/<int:pk>",UpdateSubDepartmentMasterView.as_view(),name="sub_update"),
    path("sub_delete/<int:pk>",delete_sub,name="sub_delete"),

    path("emp_mas",EmployeeMasterView.as_view(),name="emp_mas"),
    path("emp_add",EmployeeCreateView.as_view(),name="emp_add"),
    path("emp_list",EmployeeListView.as_view(),name="emp_list"),
    path("emp_update/<int:pk>",UpdateEmployeeListView.as_view(),name="emp_update"),
    path("emp_delete/<int:pk>",delete_employee,name="emp_delete"),
    
    path("logout",sign_out_view,name="sign-out"),


]
