from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cube/', views.cube, name='cube'),
    path('coin/', views.coinflip, name='coinflip'),
    path('number/', views.random_number, name='random_number'),
]