from django.contrib import admin
from .models import Role, User, Department, Employee, Project
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
