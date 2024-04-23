from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('set/', views.set_authors, name='set'),
]
