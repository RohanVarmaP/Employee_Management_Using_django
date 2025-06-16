from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.role_name == 'admin'


class IsHOD(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.role_name == 'hod'


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.role_name == 'employee'
