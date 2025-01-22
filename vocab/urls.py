from django.urls import path
from . import views

app_name = 'vocab'

urlpatterns = [
    path('', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('progress/', views.my_progress, name='my_progress'),
]