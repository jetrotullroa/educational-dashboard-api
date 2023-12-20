from django.db import models

# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Teacher(models.Model):
	name = models.CharField(max_length=100)
	year_of_experience = models.IntegerField(default=0)
	subjects = models.ManyToManyField(Subject)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Coach(models.Model):
	name = models.CharField(max_length=100)
	year_of_experience = models.IntegerField(default=0)
	specialization = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class StudentProgress(models.Model):
	class_id = models.IntegerField(default=0)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	average_score_improvement = models.IntegerField(default=0)
	homework_completion_rate = models.IntegerField(default=0)
	attendance_rate = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class ResourceManagement(models.Model):
	name=models.CharField(max_length=100)
	allocated_teachers=models.ManyToManyField(Teacher)
	utilization_rate=models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class TeacherActivities(models.Model):
	teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
	last_active=models.DateTimeField()
	activity_score=models.IntegerField(default=0)
	student_interaction_rating=models.CharField(max_length=5)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class CoachTeacherInteraction(models.Model):
	teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
	coach=models.ForeignKey(Coach, on_delete=models.CASCADE)
	last_meeting_date=models.DateTimeField()
	meeting_notes=models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)