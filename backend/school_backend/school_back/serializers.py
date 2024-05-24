# serializers.py

from rest_framework import serializers
from .models import Course, Student, Teacher
from .models import Student, Teacher



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        
        
