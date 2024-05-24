# urls.py

from django.urls import path
from .views import (
    CourseCreateAPIView, BulkAssignStudentsAPIView, BulkDeassignStudentsAPIView,
    BulkCreateTeachersAPIView, BulkAssignCoursesToTeachersAPIView, BulkDeassignCoursesFromTeachersAPIView,
    StudentListAPIView, TeacherListAPIView ,StudentCoursesAPIView ,TeacherCoursesAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/admin/courses/create/', CourseCreateAPIView.as_view(), name='admin-create-course'),
    path('api/admin/courses/bulk-assign-students/', BulkAssignStudentsAPIView.as_view(), name='admin-bulk-assign-students'),
    path('api/admin/courses/bulk-deassign-students/', BulkDeassignStudentsAPIView.as_view(), name='admin-bulk-deassign-students'),
    path('api/admin/teachers/bulk-create/', BulkCreateTeachersAPIView.as_view(), name='admin-bulk-create-teachers'),
    path('api/admin/teachers/bulk-assign-courses/', BulkAssignCoursesToTeachersAPIView.as_view(), name='admin-bulk-assign-courses'),
    path('api/admin/teachers/bulk-deassign-courses/', BulkDeassignCoursesFromTeachersAPIView.as_view(), name='admin-bulk-deassign-courses'),
    path('api/admin/students/', StudentListAPIView.as_view(), name='admin-list-students'),
    path('api/admin/teachers/', TeacherListAPIView.as_view(), name='admin-list-teachers'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/StudentInfo/<str:pk>',StudentCoursesAPIView.as_view(),name = 'admin-student'),
    path('api/TeacherInfo/<str:pk>',TeacherCoursesAPIView.as_view(),name = 'admin-student'),
]