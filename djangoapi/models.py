from django.db import models

# Create your models here.
class Department(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)

class Employee(models.Model):
    EmployeetId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=500)
    Department=models.CharField(max_length=500)
    DateofJoining=models.DateField()
    PhotoName=models.CharField(max_length=500)



