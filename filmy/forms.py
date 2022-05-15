from django.forms import ModelForm
from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'year', 'desc', 'rating_imdb', 'poster']
