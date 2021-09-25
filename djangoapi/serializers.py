from rest_framework import serializers
from djangoapi.models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('EmployeetId','EmployeeName','Department','DateofJoining','PhotoName')





    