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
from filmy import views

urlpatterns = [
    path('all/', views.all_films_view, name='all_films_view'),
    path('new/', views.new_film_view, name='new_film_view'),
    path('edit/<int:id>', views.edit_film_view, name='edit_film_view'),
    path('delete/<int:id>', views.delete_film_view, name='delete_film_view'),
    path('details/<int:id>', views.film_details_view, name='film_details_view'),
    path('new_actor/', views.new_actor_view, name='new_actor_view'),
    path('add_actor_to_film/<int:id>', views.add_actor_to_film_view, name='add_actor_to_film_view')
]
