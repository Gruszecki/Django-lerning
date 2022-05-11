from django.shortcuts import render
from django.http import HttpResponse
from .models import Film


def all_films_view(request):
    dynamic = 'Dynamic content'
    films = Film.objects.all()
    return render(request, 'filmy.html', {'dynamic_content': dynamic, 'films': films})
