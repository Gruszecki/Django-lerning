from django.forms import ModelForm
from .models import Film, AdditionalInfo, Rating, Actor


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'year', 'desc', 'rating_imdb', 'poster']


class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['runtime', 'genre']


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'review']


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'surname']
