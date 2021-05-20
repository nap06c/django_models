from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
import datetime

class School(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name

class Certificate_type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.type

class Student(models.Model):
    fullname = models.CharField(max_length=80)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, null=True, on_delete=SET_NULL)
    grade = models.ForeignKey(Grade, null=True, on_delete=SET_NULL)
    certificate = models.ForeignKey(Certificate_type, null=True, on_delete=SET_NULL)
    school = models.ForeignKey(School, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.fullname

