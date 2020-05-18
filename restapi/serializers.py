from rest_framework import serializers
from .models import Subject, Teacher, Question, Student, Comment, Rate, Answer

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
    
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rate 
    fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer 
    fields = '__all__'