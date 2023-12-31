from rest_framework import serializers
from base.models import Subject, Teacher, Student, Coach, StudentProgress, ResourceManagement, TeacherActivities, CoachTeacherInteraction

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
	subjects = SubjectSerializer(many=True, read_only=True)

	class Meta:
		model = Teacher
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coach
		fields = '__all__'

class StudentProgressSerializer(serializers.ModelSerializer):
	subject = SubjectSerializer(many=False, read_only=True)
	student = StudentSerializer(many=False, read_only=True)
	class Meta:
		model = StudentProgress
		fields = '__all__'

class ResourceManagementSerializer(serializers.ModelSerializer):
	allocated_teachers = TeacherSerializer(many=True, read_only=True)
	class Meta:
		model = ResourceManagement
		fields = '__all__'

class TeacherActivitiesSerializer(serializers.ModelSerializer):
	teacher = TeacherSerializer(many=False, read_only=True)
	class Meta:
		model = TeacherActivities
		fields = '__all__'

class CoachTeacherInteractionSerializer(serializers.ModelSerializer):
	teacher = TeacherSerializer(many=False, read_only=True)
	coach = CoachSerializer(many=False, read_only=True)
	class Meta:
		model = CoachTeacherInteraction
		fields = '__all__'