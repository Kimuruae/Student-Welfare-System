from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterStudentView, EmergencyReportView

from .views import LoginView

urlpatterns = [
    path('', views.getData),
    path('admin/register/', views.register_admin, name='register_admin'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('emergency-report/', EmergencyReportView.as_view(), name='emergency-report'),
    path('register/', RegisterStudentView.as_view(), name='student-register'),
]