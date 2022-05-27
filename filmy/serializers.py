from rest_framework import serializers
from .models import Film, Actor


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'year', 'desc']


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['first_name', 'surname']
