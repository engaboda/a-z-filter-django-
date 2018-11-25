from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id' , 'username' , 'first_name' , 'address' , 'age']
    list_filter = ['id' , 'username']
    search_fields = ['id' , 'username']
    # change_form_template = 
admin.site.register(Employee , EmployeeAdmin)
