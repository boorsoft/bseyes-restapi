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

  def __str__(self):
    return self.comment

class Rate(models.Model):
  rate_id = models.AutoField(primary_key=True)
  rate = models.IntegerField()

  def __str__(self):
    return self.rate

class Answer(models.Model):
  answer_id = models.AutoField(primary_key=True)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  question = models.ManyToManyField(Question)
  rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.answer_id