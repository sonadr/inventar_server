from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              # Главная страница
    path('registration/', views.registration, name='registration'),  # Страница регистрации
    path('confirmation/', views.confirmation, name='confirmation'),  # Страница подтверждения
]
