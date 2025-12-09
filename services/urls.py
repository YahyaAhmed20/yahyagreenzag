
from django.urls import path

from . import views


app_name = 'services'

urlpatterns = [
    path('', views.services, name='services'),
    path('service_detail/', views.service_detail, name='service_detail'),

  

    
]