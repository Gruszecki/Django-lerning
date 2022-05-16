from django.shortcuts import render, get_object_or_404, redirect
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
        return redirect(all_films_view)

    return render(request, 'new_film.html', {'form': form})


def edit_film_view(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_films_view)

    return render(request, 'new_film.html', {'form': form})


