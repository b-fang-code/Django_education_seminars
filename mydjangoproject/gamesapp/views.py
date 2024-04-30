from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime
from . import models, forms


def index(request):
    if request.method == 'POST':
        form = forms.GameForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            count = form.cleaned_data['count']
            if choice == 'C':
                return get_n_coins(request, count)
            elif choice == 'K':
                return get_n_cubes(request, count)
            elif choice == 'N':
                return get_n_numbers(request, count)
    else:
        form = forms.GameForm()
    return render(request, 'gamesapp/index.html', {'form': form})


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
