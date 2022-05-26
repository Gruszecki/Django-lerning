from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Film, AdditionalInfo, Rating, Actor
from .forms import FilmForm, AdditionalInfoForm, RatingForm, ActorForm
from django.contrib.auth.decorators import login_required


def get_film_with_ratings(films):
    avg_ratings = []

    for film in films:
        ratings = Rating.objects.filter(film=film)
        avg_temp_sum = sum([Rating._meta.get_field('rating').value_from_object(rating) for rating in ratings])
        avg_temp = avg_temp_sum / len(ratings) if len(ratings) > 0 else 0
        avg_ratings.append((film, f'{avg_temp:.2f}'))

    return avg_ratings


def all_films_view(request):
    films = Film.objects.all()
    film_with_ratings = get_film_with_ratings(films)

    return render(request, 'filmy.html', {'films_length': len(films), 'film_with_ratings': film_with_ratings})


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

    return render(request, 'film-edit.html', {'film_form': film_form, 'info_form': info_form, 'is_new': True})


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

    return render(request, 'film-edit.html', {'film_form': film_form, 'info_form': info_form, 'is_new': False, 'film': film})


@login_required()
def delete_film_view(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(all_films_view)

    return render(request, 'confirm.html', {'film': film})


def get_avg_rating(film):
    ratings = Rating.objects.filter(film=film)
    ratings_sum = sum([Rating._meta.get_field('rating').value_from_object(rating) for rating in ratings])
    avg_rating = ratings_sum / len(ratings) if len(ratings) > 0 else 0

    return f'{avg_rating:.2f}'


def get_film_reviews(film):
    ratings = Rating.objects.filter(film=film)
    reviews = [Rating._meta.get_field('review').value_from_object(rating) for rating in ratings]

    return reviews


def film_details_view(request, id):
    film = get_object_or_404(Film, pk=id)
    actors = film.actors.all()
    reviews = get_film_reviews(film)
    avg_rating = get_avg_rating(film)
    rating_form = RatingForm(request.POST or None)

    try:
        info = AdditionalInfo.objects.get(film=film.id)
    except AdditionalInfo.DoesNotExist:
        info = None

    if request.method == 'POST':
        try:
            rating = rating_form.save(commit=False)
            rating.film = film
            rating.save()
        except ValueError as err:
            print(err)
        finally:
            rating_form = RatingForm(None)
            avg_rating = get_avg_rating(film)
            return redirect(film_details_view, film.id)

    return render(request, 'film-details.html', {'film': film, 'rating': avg_rating, 'info': info, 'rating_form': rating_form, 'reviews': reviews, 'actors': actors})


@login_required()
def new_actor_view(request):
    actor_form = ActorForm(request.POST or None)

    if actor_form.is_valid():
        actor_form.save()
        return redirect(new_actor_view)

    return render(request, 'new-actor.html', {'actor_form': actor_form})


@login_required()
def add_actor_to_film_view(request, id):
    actors = Actor.objects.all().order_by('surname')
    film = Film.objects.get(id=id)
    saved_actors = film.actors.all()

    if request.method == 'POST':
        selected_actors = request.POST.getlist("actors")
        for actor in saved_actors:
            if str(actor.id) not in selected_actors:
                film.actors.remove(Actor.objects.get(id=actor.id))
                film.save()
        for actor_id in selected_actors:
            film.actors.add(Actor.objects.get(id=actor_id))
            film.save()

        messages.success(request, f'Actors added to {film.title}')
        return redirect(film_details_view, film.id)

    return render(request, 'add-actor-to-film.html', {'film': film, 'actors': actors, 'saved_actors': saved_actors})