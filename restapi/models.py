from django.db import models
from django.utils import timezone
import secrets

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
    return self.last_name + " " + self.first_name

class Question(models.Model):
  question_id = models.AutoField(primary_key=True)
  question_body = models.CharField(max_length=300)

  def __str__(self):
    return self.question_body

class Student(models.Model):
  student_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=50, null=True)
  password = models.CharField(max_length=100, null=True)
  subject = models.ManyToManyField(Subject)

  def __str__(self):
    return self.username

class Comment(models.Model):
  comment_id = models.AutoField(primary_key=True)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  comment = models.TextField()
  create_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.comment

class Answer(models.Model):
  answer_id = models.AutoField(primary_key=True)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  question = models.ManyToManyField(Question)
  rate = models.CharField(max_length=100, blank=True)
  comment = models.TextField(blank=True)
  create_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(self.answer_id)

class StudentTokenModel(models.Model):
  key = models.CharField("Key", max_length=40, primary_key=True)
  student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name="Student")
  created = models.DateTimeField("Created", auto_now_add=True)

  class Meta:
    verbose_name = "Token"
    verbose_name_plural = "Tokens"

  def save(self, *args, **kwargs):
    if not self.key:
        self.key = self.generate_key()
    return super(StudentTokenModel, self).save(*args, **kwargs)

  def generate_key(self):
    return secrets.token_hex(16)

  def __str__(self):
    return str(self.key)