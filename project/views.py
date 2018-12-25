from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView

from .models import Employee
from .serializers import GroupSerializer, EmployeeSerializer, EmployeeCreate, EmployeeUpdate


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CreateEmployee(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreate


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeUpdate


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
