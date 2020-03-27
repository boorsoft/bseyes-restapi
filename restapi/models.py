from django.db import models

class Teacher(models.Model):
  teacher_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)

class Subject(models.Model):
  subject_id = models.AutoField(primary_key=True)
  sub_name = models.CharField(max_length=100)
  teacher = models.ManyToManyField(Teacher)

class Question(models.Model):
  question_id = models.AutoField(primary_key=True)
  question_body = models.CharField(max_length=300)
  rate = models.IntegerField()