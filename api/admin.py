from django.contrib import admin
from .models import Students

# Register your models here.

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'City', 'Age', 'Roll_Number', 'School_Name']
