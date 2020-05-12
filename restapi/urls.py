from rest_framework import routers
from django.urls import path
from . import views
from .api import SubjectViewSet, TeacherViewSet, QuestionViewSet, AnswerViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('api/subjects', SubjectViewSet, 'subjects')
router.register('api/teachers', TeacherViewSet, 'teachers')
router.register('api/questions', QuestionViewSet, 'questions')
router.register('api/answers', AnswerViewSet, 'answers')
router.register('api/students', StudentViewSet, 'students')

urlpatterns = router.urls
