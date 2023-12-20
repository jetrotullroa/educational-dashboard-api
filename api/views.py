from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Subject, Teacher, Student, Coach, Student, StudentProgress
from .serializers import SubjectSerializer, TeacherSerializer, StudentSerializer, CoachSerializer, StudentProgressSerializer

@api_view(['GET'])
def subjects(request):
	subjects = Subject.objects.all()
	serializer = SubjectSerializer(subjects, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def teachers(request):
	teachers = Teacher.objects.all()
	serializer = TeacherSerializer(teachers, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def teacher(request, **kwargs):
	teacher = Teacher.objects.get(id=kwargs['teacher_id'])
	serializer = TeacherSerializer(teacher, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def coaches(request):
	coaches = Coach.objects.all()
	serializer = CoachSerializer(coaches, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def coach(request, **kwargs):
	coach = Coach.objects.get(id=kwargs['coach_id'])
	serializer = CoachSerializer(coach, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def students(request):
	students = Student.objects.all()
	serializer = StudentSerializer(students, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def studentProgress(request, **kwargs):
	student_progress = StudentProgress.objects.filter(student_id=kwargs['student_id'])
	serializer = StudentProgressSerializer(student_progress, many=True)
	return Response(serializer.data)
