from rest_framework import serializers
from .models import Subject, Teacher, Question, Answer, Student

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject
    fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = '__all__'
    
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'