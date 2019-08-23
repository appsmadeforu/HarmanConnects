from django.contrib import admin

from .models import Employee, Project, Department


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'username', 'first_name', 'last_name', 'dob', 'email']


admin.site.register(Employee, EmployeeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['proj_name', 'proj_link', 'proj_description', 'proj_start_date']


admin.site.register(Project, ProjectAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['empl']


admin.site.register(Department, DepartmentAdmin)