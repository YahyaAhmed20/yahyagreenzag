from django.urls import path
from . import views

app_name = 'ourproject'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_details, name='project_details'),  # صفحة تفاصيل المشروع
]