from rest_framework import routers
from .api import SubjectViewSet, TeacherViewSet, QuestionViewSet, AnswerViewSet, StudentViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/subjects', SubjectViewSet, 'subjects')
router.register('api/teachers', TeacherViewSet, 'teachers')
router.register('api/questions', QuestionViewSet, 'questions')
router.register('api/answers', AnswerViewSet, 'answers')
router.register('api/students', StudentViewSet, 'students')
router.register('api/comments', CommentViewSet, 'comments')

urlpatterns = router.urls
