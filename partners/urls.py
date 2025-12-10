

from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.partners, name='partners'),
    path('partner_details/', views.partner_details, name='partner_details'),
]