from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField('Student', blank=True)
    teachers = models.ManyToManyField('Teacher', blank=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    grade = models.CharField(max_length=10)
    academic_year = models.IntegerField(default=2024)
    dob = models.DateField()
    unique_student_id = models.CharField(max_length=20, unique=True)
    school_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    unique_teacher_id = models.CharField(max_length=20, unique=True)
    school_name = models.CharField(max_length=100)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/', blank=True, null=True) 
