from rest_framework.authentication import TokenAuthentication
from restapi.models import StudentTokenModel

class StudentTokenAuthentication(TokenAuthentication):
    model = StudentTokenModel