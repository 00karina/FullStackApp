from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from djangoapi.models import Department,Employee
from djangoapi.serializers import DepartmentSerializer,EmployeeSerializer

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments=Department.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializers=DepartmentSerializer(data=department_data)
        if departments_serializers.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializers=DepartmentSerializer(department,data=department_data)
        if departments_serializers.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='DELETE':
        departments=Department.objects.GET(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Sucessfully",safe=False)

           
