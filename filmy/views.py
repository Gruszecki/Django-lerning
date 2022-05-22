from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, AdditionalInfo
from .forms import FilmForm, AdditionalInfoForm
from django.contrib.auth.decorators import login_required


def all_films_view(request):
    dynamic = 'Dynamic content'
    films = Film.objects.all()
    return render(request, 'filmy.html', {'dynamic_content': dynamic, 'films': films})


@login_required()
def new_film_view(request):
    film_form = FilmForm(request.POST or None, request.FILES or None)
    info_form = AdditionalInfoForm(request.POST or None)

    if all((film_form.is_valid(), info_form.is_valid())):
        film = film_form.save(commit=False)
        info = info_form.save()
        film.additional_info = info
        film.save()
        return redirect(all_films_view)

    return render(request, 'film.html', {'film_form': film_form, 'info_form': info_form, 'is_new': True})


@login_required()
def edit_film_view(request, id):
    film = get_object_or_404(Film, pk=id)

    try:
        info = AdditionalInfo.objects.get(film=film.id)
    except AdditionalInfo.DoesNotExist:
        info = None

    film_form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    info_form = AdditionalInfoForm(request.POST or None, instance=info)

    if film_form.is_valid():
        film.poster = 'posters/default.jpg' if not film.poster else film.poster
        film = film_form.save(commit=False)
        info = info_form.save()
        film.additional_info = info
        film.save()
        return redirect(all_films_view)

    return render(request, 'film.html', {'film_form': film_form, 'info_form': info_form, 'is_new': False, 'film': film})


@login_required()
def delete_film_view(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(all_films_view)

    return render(request, 'confirm.html', {'film': film})
