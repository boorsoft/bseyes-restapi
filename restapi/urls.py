from rest_framework import routers
from django.urls import path
from .api import SubjectView, TeacherView, QuestionViewSet, StudentViewSet,  AnswerViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/questions', QuestionViewSet, 'questions')
router.register('api/students', StudentViewSet, 'students')
router.register('api/answers', AnswerViewSet, 'answers')

urlpatterns = router.urls
urlpatterns += [
  path('api/subjects', SubjectView.as_view()),
  path('api/teachers', TeacherView.as_view()),
  path('admin/subjects/', views.subjects, name='subjects'),
  path('admin/subjects/<int:id>/teachers', views.teachers, name='teachers'),
  path('admin/subjects/<int:subject_id>/teachers/<int:teacher_id>/result', views.result, name='result')
]
