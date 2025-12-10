from django.urls import path
from . import views
from .views import *

# calculate_tray_manual

app_name = 'news'

urlpatterns = [
    path('', views.news, name='news'),
    path('news_detail/', views.news_details, name='news_detail'),



]
