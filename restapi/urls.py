from django.urls import path
from rest_framework import routers
from .api import SubjectView, TeacherView, QuestionView, StudentView,  AnswerView
from . import views

router = routers.DefaultRouter()
router.register('api/students', StudentView, 'students')

urlpatterns = [
  path('api/subjects', SubjectView.as_view()),
  path('api/teachers', TeacherView.as_view()),
  path('api/answers', AnswerView.as_view()),
  path('api/questions', QuestionView.as_view()),
  path('admin/subjects/', views.subjects, name='subjects'),
  path('admin/subjects/<int:id>/teachers', views.teachers, name='teachers'),
  path('admin/subjects/<int:subject_id>/teachers/<int:teacher_id>/result', views.result, name='result')
]

urlpatterns += router.urls