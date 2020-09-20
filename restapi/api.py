from restapi.models import Subject, Teacher, Question, Student, Answer, StudentTokenModel
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubjectSerializer, TeacherSerializer, QuestionSerializer, StudentSerializer, AnswerSerializer

class SubjectView(APIView):
  def get(self, request, format=None):
    student_token_model = StudentTokenModel.objects.all()
    tokens = []

    for el in student_token_model:
      tokens.append(el.key)
  
    auth = request.headers.get('Authorization')

    if str(auth).strip('Token ') in tokens:
      queryset = Subject.objects.all()
      serializer_class = SubjectSerializer(queryset, many=True)
      return Response(serializer_class.data)
    else:
      return Response({'error': 'Invalid token, or no token provided.'});

class TeacherView(APIView):
  def get(self, request, format=None):
    student_token_model = StudentTokenModel.objects.all()
    tokens = []

    for el in student_token_model:
      tokens.append(el.key)
  
    auth = request.headers.get('Authorization')

    if str(auth).strip('Token ') in tokens:
      queryset = Teacher.objects.all()
      serializer_class = TeacherSerializer(queryset, many=True)
      return Response(serializer_class.data)
    else:
      return Response({'error': 'Invalid token, or no token provided.'});


class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]

class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [
    permissions.IsAdminUser
  ]

class AnswerView(APIView):
  def get(self, request, format=None):
    student_token_model = StudentTokenModel.objects.all()
    tokens = []

    for el in student_token_model:
      tokens.append(el.key)
  
    auth = request.headers.get('Authorization')

    if str(auth).strip('Token ') in tokens:
      queryset = Answer.objects.all()
      serializer_class = AnswerSerializer(queryset, many=True)
      return Response(serializer_class.data)
    else:
      return Response({'error': 'Invalid token, or no token provided.'});

  def post(self, request, format=None):
    student_token_model = StudentTokenModel.objects.all()
    tokens = []

    for el in student_token_model:
      tokens.append(el.key)
  
    auth = request.headers.get('Authorization')

    if str(auth).strip('Token ') in tokens:
      serializer = AnswerSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Invalid token, or no token provided.'})

# class AnswerViewSet(viewsets.ModelViewSet):
#   queryset = Answer.objects.all()
#   serializer_class = AnswerSerializer
#   permission_classes = [
#     permissions.IsAuthenticated
#   ]


