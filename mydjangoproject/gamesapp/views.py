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


def cube(request):
    return HttpResponse(random.randint(1, 6))


def random_number(request):
    return HttpResponse(random.randint(0, 100))


def get_last_n_coins(request):
    return HttpResponse(models.Coin.get_last_n_coins(5))
