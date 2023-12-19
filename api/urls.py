from django.urls import path
from . import views

urlpatterns = [
	path('v1/subjects', views.subjects, name='api-subjects-data'),
]