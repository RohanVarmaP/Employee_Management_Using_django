# apis/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, UserViewSet, DepartmentViewSet,
    EmployeeViewSet, ProjectViewSet, EmployeeProfileViewSet
)

router = DefaultRouter()
router.register('roles', RoleViewSet)
router.register('users', UserViewSet)
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)
router.register('projects', ProjectViewSet)

# ✅ Provide unique basename to avoid collision
router.register('profiles', EmployeeProfileViewSet, basename='employee-profile')

urlpatterns = [
    path('', include(router.urls)),
]
