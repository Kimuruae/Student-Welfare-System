from django.urls import path
from . import views
from .views import login_user
from .views import RegisterStudentView, EmergencyReportView

urlpatterns=[
     path('', views.getData),
     
]
urlpatterns= [
    path('api/admin/register/', views.register_admin, name='register_admin'),
]

urlpatterns = [
    path('api/login/', login_user, name='login'),
]
urlpatterns = [
    path('api/register/', RegisterStudentView.as_view(), name='student-register'),
]
urlpatterns = [
    path('api/emergency-report/', EmergencyReportView.as_view()),
]