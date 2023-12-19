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