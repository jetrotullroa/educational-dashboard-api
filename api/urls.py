from django.urls import path
from . import views

urlpatterns = [
	path('v1/subjects', views.subjects, name='api-subjects-data'),
	path('v1/teachers', views.teachers, name='api-teachers-data'),
	path('v1/teachers/<teacher_id>', views.teacher, name='api-teachers-data'),
	path('v1/coaches', views.coaches, name='api-subjects-data'),
	path('v1/coach/<coach_id>', views.coach, name='api-teachers-data'),
	path('v1/students', views.students, name='api-teachers-data'),
]