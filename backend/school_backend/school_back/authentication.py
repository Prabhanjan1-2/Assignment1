# authentication.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Student, Teacher
from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UniqueIDDOBBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            student = Student.objects.get(unique_student_id=username, dob=password)
            user, _ = User.objects.get_or_create(username=student.unique_student_id)
            return user
        except ObjectDoesNotExist:
            try:

                teacher = Teacher.objects.get(unique_teacher_id=username, dob=password)
                user, _ = User.objects.get_or_create(username=teacher.unique_teacher_id)
                return user
            except ObjectDoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



