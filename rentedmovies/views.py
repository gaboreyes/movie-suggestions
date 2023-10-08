from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RentedMovie
from .serializers import RentedMoviesSerializer

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
        # TODO: Allows a user to rent a movie
        return Response({ "foo": "bar" })
