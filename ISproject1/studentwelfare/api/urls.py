from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterStudentView, EmergencyReportView

from .views import LoginView

print("✅ api.urls loaded!")
urlpatterns=[
     path('', views.getData),
     
]
urlpatterns= [
    path('api/admin/register/', views.register_admin, name='register_admin'),
]


urlpatterns = [
    path('login/', LoginView, name='api-login'),
]



urlpatterns = [
    path('api/emergency-report/', EmergencyReportView.as_view()),
]
urlpatterns = [
    path('api/register/', RegisterStudentView.as_view(), name='student-register'),
]