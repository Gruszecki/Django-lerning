from django.contrib import admin
from .models import Film


# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'rating_imdb']
    list_filter = ['year']
    search_fields = ['title', 'desc']
