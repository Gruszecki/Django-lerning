"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from filmy.views import all_films_view, new_film_view, edit_film_view, delete_film_view, film_details_view, new_actor_view

urlpatterns = [
    path('all/', all_films_view, name='all_films_view'),
    path('new/', new_film_view, name='new_film_view'),
    path('edit/<int:id>', edit_film_view, name='edit_film_view'),
    path('delete/<int:id>', delete_film_view, name='delete_film_view'),
    path('details/<int:id>', film_details_view, name='film_details_view'),
    path('new_actor/', new_actor_view, name='new_actor_view')
]
