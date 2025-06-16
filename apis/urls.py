from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RoleViewSet, UserViewSet, DepartmentViewSet, EmployeeViewSet,
    ProjectViewSet, LoginView, LogoutView, EmployeeProfileViewSet
)

router = DefaultRouter()
router.register('roles', RoleViewSet, basename='role')
router.register('users', UserViewSet, basename='user')
router.register('departments', DepartmentViewSet, basename='department')
router.register('employees', EmployeeViewSet, basename='employee')
router.register('projects', ProjectViewSet, basename='project')
router.register('profiles', EmployeeProfileViewSet, basename='employee_profile')

urlpatterns = [
    path('', include(router.urls)),

    # Auth URLs with explicit names
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
