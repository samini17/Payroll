from django.contrib import admin

from .models import Department, Degree, Employee, SalaryPayment, Furlough


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'is_active', 'established_date']
    list_editable = ['is_active']


class DegreeAdmin(admin.TabularInline):
    model = Degree
    fields = ('degree', 'branch', 'start_date', 'end_date')
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'job_title', 'date_joined']
    inlines = [DegreeAdmin]
    ordering = ['-date_joined']
    list_filter = ['job_title', 'marital_status']
    search_fields = ['last_name', 'phone_number']
    date_hierarchy = 'date_joined'
    list_editable = ['job_title']
    list_display_links = ['last_name']


@admin.register(SalaryPayment)
class SalaryPaymentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'work_time', 'from_date', 'till_date']
    date_hierarchy = 'till_date'
    ordering = ['-work_time']


@admin.register(Furlough)
class FurloughView(admin.ModelAdmin):
    list_display = ['employee', 'is_approved', 'from_date', 'till_date']
