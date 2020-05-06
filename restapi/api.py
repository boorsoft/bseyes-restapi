from restapi.models import Subject, Teacher, Question, Answer, Student
from rest_framework import viewsets, permissions
from .serializers import SubjectSerializer, TeacherSerializer, QuestionSerializer, AnswerSerializer, StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly,
  ]

class TeacherViewSet(viewsets.ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]

class AnswerViewSet(viewsets.ModelViewSet):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer
  permissions_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]

class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [
    permissions.IsAuthenticated
  ]
