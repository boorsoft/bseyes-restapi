from rest_framework import routers
from .api import SubjectViewSet, TeacherViewSet, QuestionViewSet, StudentViewSet, CommentViewSet, RateViewSet, AnswerViewSet

router = routers.DefaultRouter()
router.register('api/subjects', SubjectViewSet, 'subjects')
router.register('api/teachers', TeacherViewSet, 'teachers')
router.register('api/questions', QuestionViewSet, 'questions')
router.register('api/students', StudentViewSet, 'students')
router.register('api/comments', CommentViewSet, 'comments')
router.register('api/rate', RateViewSet, 'rate')
router.register('api/answers', AnswerViewSet, 'answers')

urlpatterns = router.urls
