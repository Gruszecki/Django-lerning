from django.forms import ModelForm
from .models import Film, AdditionalInfo


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'year', 'desc', 'rating_imdb', 'poster']


class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['runtime', 'genre']
