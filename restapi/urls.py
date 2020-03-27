from rest_framework import routers
from .api import SubjectViewSet, TeacherViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register('subjects', SubjectViewSet, 'subjects')
router.register('teachers', TeacherViewSet, 'teachers')
router.register('questions', QuestionViewSet, 'questions')

urlpatterns = router.urls