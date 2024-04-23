from django.shortcuts import render
from django.http import HttpResponse
from . import models
from datetime import datetime


def set_authors(request):
    for i in range(10):
        author = models.Author.objects.create(name=f'Автор {i}', surname=f'Фамилия {i}', email=f'автор{i}@mail.ru',
                                              bio=f'Биография {i}', birthday=datetime.now(),
                                              full_name=f'Автор {i} Фамилия {i}')
        author.save()
    return HttpResponse("Авторы добавлены")


def index(request):
    return HttpResponse("Blog")


def authors(request):
    return HttpResponse("Authors")
