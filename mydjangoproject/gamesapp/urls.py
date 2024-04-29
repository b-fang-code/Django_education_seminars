from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cube/', views.cube, name='cube'),
    path('coin/', views.coinflip, name='coinflip'),
    path('number/', views.random_number, name='random_number'),
    path('last/', views.get_last_n_coins, name='last_coins'),
    path('number/<int:count>/', views.get_n_numbers, name='get_n_numbers'),
    path('cube/<int:count>/', views.get_n_cubes, name='get_n_cubes'),
    path('coin/<int:count>/', views.get_n_coins, name='get_n_coins'),
]