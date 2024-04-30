from django.shortcuts import render
from django.http import HttpResponse
from . import models
from datetime import datetime
from . import forms


def set_authors(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            full_name = form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']
            author = models.Author(name=name, surname=surname, email=email, bio=bio, birthday=birthday,
                                   full_name=full_name)
            author.save()
    else:
        form = forms.AuthorForm()
    return render(request, 'blogapp/add_author_form.html', {'form': form})


def index(request):
    return HttpResponse("Blog")


def authors(request):
    return HttpResponse("Authors")
