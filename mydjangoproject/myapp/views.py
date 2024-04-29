from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Main page',
        'name': 'Pavel',
    }
    return render(request, 'myapp/index.html', context)


def about(request):
    context = {
        'title': 'About me',
        'number': 1
    }
    return render(request, 'myapp/about.html', context)
