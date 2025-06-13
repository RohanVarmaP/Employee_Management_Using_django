# apis/serializers.py
from rest_framework import serializers
from .models import User, Role, Department, Employee, Project

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    dept = DepartmentSerializer()
    role = RoleSerializer()
    reporting_to = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    assigned_to = EmployeeSerializer()

    class Meta:
        model = Project
        fields = '__all__'


# Profile serializer to show employee full profile
class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    dept = DepartmentSerializer()
    role = RoleSerializer()
    projects = ProjectSerializer(many=True)
    reporting_to = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = '__all__'
