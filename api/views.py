from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import MovieSerializer
from movies.models import Movie
from . import serializers


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


class MoviesView(APIView):
    """
    Foo
    """

    def get(self, request):
        """
        Foo
        """
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Foo
        """
        serializer = MovieSerializer(data=request.data)
        message = 'Oops, something went wrong!'
        response_data = None
        if serializer.is_valid():
            serializer.save()
            message = 'Entry saved!'
            response_data = request.data
        return Response({"message": message, "data": response_data})
