from restapi.models import Subject, Teacher, Question
from rest_framework import viewsets
from .serializers import SubjectSerializer, TeacherSerializer, QuestionSerializer

class SubjectViewSet(viewsets.ModelViewSet):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer