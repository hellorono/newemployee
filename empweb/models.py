from django.db import models


class Departmentmaster(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    created_by_date=models.DateField()
    created_at_date=models.DateField()

    def __str__(self):
        return self.department_name


class SubDepartmentmaster(models.Model):
    sub_department_id=models.AutoField(primary_key=True)
    department_id=models.ForeignKey(Departmentmaster, on_delete=models.CASCADE)
    sub_department_name=models.CharField(max_length=110)
    description=models.CharField(max_length=100)
    created_by_date=models.DateField()
    created_at_date=models.DateField()

    def __str__(self):
        return self.sub_department_name











    

