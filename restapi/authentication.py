from rest_framework.authentication import TokenAuthentication
from restapi.models import StudentTokenModel

class StudentTokenAthentication(TokenAuthentication):
    model = StudentTokenModel