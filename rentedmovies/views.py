from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RentedMovie
from .serializers import RentedMoviesSerializer
from django.contrib.auth.models import User
from movies.models import Movie
import datetime


class RentMovie(APIView):
    """
    Allows users the renting of movies via POST.
    """

    def get(self, request):
        """
        Returns the amount of rented movies if the user hitting the endpoint is admin.
        """
        # TODO: Returns the amount of rented movies if the user hitting the endpoint is admin
        queryset = RentedMovie.objects.all()
        serializer = RentedMoviesSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Allows a user to rent a movie
        """
        try:
            movie_id = request.data.get('movie')
            user_id = request.data.get('user')
            renting_days = request.data.get('renting_days')
            rented_until = datetime.datetime.utcnow() + datetime.timedelta(days=renting_days)
            movie_record = Movie.objects.get(pk=movie_id)
            user_record = User.objects.get(pk=user_id)
            RentedMovie.objects.create(movie_id=movie_record, user_id=user_record, rented_until=rented_until)
            message = "Movie rented successfully!"
        except Exception as e: 
            print(e)
            message = "Something went wrong."
        return Response({"message": message})
