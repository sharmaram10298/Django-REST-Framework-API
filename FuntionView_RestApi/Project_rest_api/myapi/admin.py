from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age','gender','phone_number', 'education','address','city','state','country', 'salary_annul_ctc')

