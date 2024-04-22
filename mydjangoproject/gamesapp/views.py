from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return HttpResponse("Games")


def coinflip(request):
    return HttpResponse(random.choice(['Орел', 'Решка']))


def cube(request):
    return HttpResponse(random.randint(1, 6))


def random_number(request):
    return HttpResponse(random.randint(0, 100))
