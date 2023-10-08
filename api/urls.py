from django.urls import path
from rest_framework import routers
from .views import UsersView, IndexView
from movies.views import MoviesView
from rentedmovies.views import RentMovie

router = routers.DefaultRouter()


urlpatterns = [
    path('users', UsersView.as_view()),
    path('movies', MoviesView.as_view()),
    path('rent-movie', RentMovie.as_view()),
    path('', IndexView.as_view()),
]
