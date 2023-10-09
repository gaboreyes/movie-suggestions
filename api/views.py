from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


class IndexView(APIView):
    """
    Dict with the existing urls for the API. Only has a GET endpoint.
    """
    def get(self, request):
        """
        Returns a dict with valid urls
        """
        valid_urls = {
            "users": "api/users/",
            "movies": "api/movies/",
            "rent-movie": "api/rent-movie/"
        }
        return Response(valid_urls)


class UsersView(APIView):
    """
    Foo
    """

    def get(self, request):
        """
        Foo
        """
        queryset = User.objects.all()
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data)
