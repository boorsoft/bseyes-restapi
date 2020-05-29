from rest_framework import routers
from django.urls import path
from .api import SubjectViewSet, TeacherViewSet, QuestionViewSet, StudentViewSet,  AnswerViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/subjects', SubjectViewSet, 'subjects')
router.register('api/teachers', TeacherViewSet, 'teachers')
router.register('api/questions', QuestionViewSet, 'questions')
router.register('api/students', StudentViewSet, 'students')
router.register('api/answers', AnswerViewSet, 'answers')

urlpatterns = router.urls
urlpatterns += [
  path('admin/results', views.results, name='results')
]
