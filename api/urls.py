from django.urls import path
from rest_framework import routers
from .views import UsersView, MoviesView


router = routers.DefaultRouter()


urlpatterns = [
    path('users', UsersView.as_view()),
    path('movies', MoviesView.as_view()),
]
