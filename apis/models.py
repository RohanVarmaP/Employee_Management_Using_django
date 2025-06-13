from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.role_name


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_head = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='headed_departments')

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    em_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    reporting_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role__role_name': 'hod'})

    def __str__(self):
        return self.name


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.project_name
