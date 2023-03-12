from django.urls import path

from .views import movie_list, movie_manip

urlpatterns = [
    path("list/", movie_list, name="movie_list"),
    path("list/<int:pk>/", movie_manip, name="movie_manip"),
]
