from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required


def all_films_view(request):
    dynamic = 'Dynamic content'
    films = Film.objects.all()
    return render(request, 'filmy.html', {'dynamic_content': dynamic, 'films': films})


@login_required()
def new_film_view(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_films_view)

    return render(request, 'film.html', {'form': form, 'is_new': True})


@login_required()
def edit_film_view(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_films_view)

    return render(request, 'film.html', {'form': form, 'is_new': False, 'film': film})


@login_required()
def delete_film_view(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(all_films_view)

    return render(request, 'confirm.html', {'film': film})
