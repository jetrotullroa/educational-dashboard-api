from django.urls import path
from . import views

urlpatterns = [
	path('v1/subjects', views.subjects, name='api-subjects-data'),
	path('v1/teachers', views.teachers, name='api-teachers-data'),
	path('v1/teachers/<teacher_id>', views.teacher, name='api-teacher-data'),
	path('v1/coaches', views.coaches, name='api-coaches-data'),
	path('v1/coaches/<coach_id>', views.coach, name='api-coach-data'),
	path('v1/students', views.students, name='api-students-data'),
	path('v1/student_progress/<student_id>', views.studentProgress, name='api-student-progress-data'),
	path('v1/resource_managements', views.resourceManagements, name='api-resource-managements-data'),
	path('v1/teacher_activities/<teacher_id>', views.teacherActivities, name='api-teacher-activities-data'),
	path('v1/coach_teacher_interactions/', views.coachTeacherInteractions, name='api-coach-teacher-interactions-data'),
]
