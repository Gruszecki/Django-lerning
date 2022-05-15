from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm


def all_films_view(request):
    dynamic = 'Dynamic content'
    films = Film.objects.all()
    return render(request, 'filmy.html', {'dynamic_content': dynamic, 'films': films})


def new_film_view(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    else:
        return render(request, 'new_film.html', {'form': form})

    return render(request, 'filmy.html', {'dynamic_content': 'Dodano nowy film', 'films': Film.objects.all()})
