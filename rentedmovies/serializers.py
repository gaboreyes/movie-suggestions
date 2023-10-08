from django.contrib.auth.models import User
from rest_framework import serializers
from .models import RentedMovie


class RentedMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedMovie
        fields = "__all__"
