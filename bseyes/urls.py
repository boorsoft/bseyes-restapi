from django.contrib import admin
from django.urls import path, include
from restapi.views import StudentAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restapi.urls')), 
    path('login/', StudentAuthentication.as_view(), name='login'),
]

urlpatterns += [
  path('auth/', include('rest_framework.urls'))
]
