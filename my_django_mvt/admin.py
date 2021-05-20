from django.contrib import admin
from .models import Student, School, Faculty, Department, Grade, Certificate_type

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Certificate_type)