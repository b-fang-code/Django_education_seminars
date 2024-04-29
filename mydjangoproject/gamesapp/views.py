from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime
from . import models


def index(request):
    return HttpResponse("Games")


def coinflip(request):
    value = models.Coin.objects.create(name=random.choice(['Орел', 'Решка']), time=datetime.now())
    value.save()
    return HttpResponse(value.name)


def get_n_coins(request, count):
    context = {'title': 'рандомные монетки', 'content': []}
    for i in range(count):
        context['content'].append(random.choice(['Орел', 'Решка']))
    return render(request, 'gamesapp/base_game.html', context)


def cube(request):
    return HttpResponse(random.randint(1, 6))


def get_n_cubes(request, count):
    context = {'title': 'рандомные кубики', 'content': []}
    for i in range(count):
        context['content'].append(random.randint(1, 6))
    return render(request, 'gamesapp/base_game.html', context)


def random_number(request):
    return HttpResponse(random.randint(0, 100))


def get_n_numbers(request, count):
    context = {'title': 'рандомные числа', 'content': []}
    for i in range(count):
        context['content'].append(random.randint(1, 100))
    return render(request, 'gamesapp/base_game.html', context)


def get_last_n_coins(request):
    return HttpResponse(models.Coin.get_last_n_coins(5))
