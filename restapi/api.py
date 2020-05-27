from restapi.models import Subject, Teacher, Question, Student, Comment, Answer
from rest_framework import viewsets, permissions
from .serializers import SubjectSerializer, TeacherSerializer, QuestionSerializer, StudentSerializer, CommentSerializer, AnswerSerializer

class SubjectViewSet(viewsets.ModelViewSet):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]

class TeacherViewSet(viewsets.ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]

class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]

class AnswerViewSet(viewsets.ModelViewSet):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]
