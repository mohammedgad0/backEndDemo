from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('empid', 'empname', 'deptname', 'email', 'ext')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')