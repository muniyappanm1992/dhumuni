from django.contrib import admin
from website.models import Employee
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.site.register(Employee)
@admin.register(Employee)
class EmpoyeeAdmin(ImportExportActionModelAdmin):
    list_display = ('name','age')
