from django.db import models

class Subject(models.Model):
  subject_id = models.AutoField(primary_key=True)
  sub_name = models.CharField(max_length=100)

  def __str__(self):
    return self.sub_name

class Teacher(models.Model):
  teacher_id = models.AutoField(primary_key=True)
  last_name = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)
  subject = models.ManyToManyField(Subject, related_name="subject")

  def __str__(self):
    return self.last_name

class Question(models.Model):
  question_id = models.AutoField(primary_key=True)
  question_body = models.CharField(max_length=300)
  
class Answer(models.Model):
  answer_id = models.AutoField(primary_key=True)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  comment = models.TextField()
  rate = models.IntegerField()