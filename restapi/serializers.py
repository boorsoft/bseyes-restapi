from rest_framework import serializers
from .models import Subject, Teacher, Question

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