
from rest_framework import generics
from rest_framework.response import Response
from .models import Course, Student, Teacher
from .serializers import CourseSerializer, StudentSerializer, TeacherSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class BulkAssignStudentsAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        student_ids = request.data.get('student_ids', [])
        course.students.set(student_ids)
        return Response({'message': 'Students assigned successfully'})

class BulkDeassignStudentsAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        student_ids = request.data.get('student_ids', [])
        course.students.remove(*student_ids)
        return Response({'message': 'Students deassigned successfully'})

class BulkCreateTeachersAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class BulkAssignCoursesToTeachersAPIView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        teacher = self.get_object()
        course_ids = request.data.get('course_ids', [])
        teacher.courses.set(course_ids)
        return Response({'message': 'Courses assigned to teacher successfully'})

class BulkDeassignCoursesFromTeachersAPIView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        teacher = self.get_object()
        course_ids = request.data.get('course_ids', [])
        teacher.courses.remove(*course_ids)
        return Response({'message': 'Courses deassigned from teacher successfully'})

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class StudentCoursesAPIView(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(unique_student_id=pk)
            print(pk)
            student_serializer = StudentSerializer(student)
            courses = student.course_set.all()  # Accessing courses through reverse relationship
            course_names = [course.name for course in courses]  # Extracting course names
            data = {
                'student': student_serializer.data,
                'courses': course_names
            }
            return Response(data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
class TeacherCoursesAPIView(APIView):
    def get(self, request, pk):
        try:
            teacher = Teacher.objects.get(unique_teacher_id=pk)
            teacher_serializer = TeacherSerializer(teacher)
            courses = teacher.course_set.all()  # Accessing courses through reverse relationship
            
            course_data = []
            for course in courses:
                course_serializer = CourseSerializer(course)
                students = course.students.all()  # Accessing students associated with the course
                student_names = [student.name for student in students]  # Extracting student names
                course_data.append({
                    'course': course_serializer.data,
                    'students': student_names
                })
                
            data = {
                'teacher': teacher_serializer.data,
                'file_url': teacher.file.url if teacher.file else None,
                'courses': course_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)