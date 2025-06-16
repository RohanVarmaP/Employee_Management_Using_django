# apis/views.py

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdmin
from .models import Role, User, Department, Employee, Project
from .serializers import (
    RoleSerializer, UserSerializer, DepartmentSerializer,
    EmployeeSerializer, ProjectSerializer, EmployeeProfileSerializer
)


# ViewSets for CRUD
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Dynamic Profile ViewSet
class EmployeeProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmployeeProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role.role_name == 'admin':
            return Employee.objects.all()

        elif user.role.role_name == 'hod':
            return Employee.objects.filter(dept=user.employee.dept)

        elif user.role.role_name == 'employee':
            return Employee.objects.filter(user=user)

        return Employee.objects.none()  # fallback


# Dynamic Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role.role_name == 'admin':
            return Project.objects.all()

        elif user.role.role_name == 'hod':
            return Project.objects.filter(assigned_to__dept=user.employee.dept)

        elif user.role.role_name == 'employee':
            return Project.objects.filter(assigned_to__user=user)

        return Project.objects.none()


# 🔐 Auth APIs
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            update_last_login(None, user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'role': user.role.role_name if hasattr(user, 'role') else None
            }, status=status.HTTP_200_OK)

        return Response({'error': "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
