from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from.models import employee
# Register your models here.
from app.models import*
class Table(ImportExportModelAdmin):
    list_display=("name","eid","email","salary")
admin.site.register(employee,Table)