import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RentedMovie
from .serializers import RentedMoviesSerializer
from movies.models import Movie



class RentMovie(APIView):
    """ Allows users the renting of movies via POST. """

    def get(self, request):
        """ Returns the amount of rented movies if the user hitting the endpoint is admin. """
        # TODO: Returns the amount of rented movies if the user hitting the endpoint is admin
        queryset = RentedMovie.objects.all()
        serializer = RentedMoviesSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ Allows a user to rent a movie """
        try:
            user_id = request.data.get("user")
            movie_id = request.data.get("movie")
            renting_days = request.data.get("renting_days")
            if movie_id == None or user_id == None or renting_days == None:
                message = "Invalid payload"
            else:
                rented_until = timezone.now() + datetime.timedelta(days=renting_days)
                # TODO: check if desired movie is in cache and run LRU script
                movie_record = Movie.objects.get(pk=movie_id)
                user_record = User.objects.get(pk=user_id)
                RentedMovie.objects.create(movie_id=movie_record, user_id=user_record, rented_until=rented_until)
                message = "Movie rented successfully!"
        except Exception as e: 
            print(e)
            message = "Something went wrong"
        return Response({"message": message})
