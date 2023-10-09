from rest_framework.response import Response
from rest_framework.views import APIView
from movies.serializers import MovieSerializer
from movies.models import Movie

# Create your views here.


class MoviesView(APIView):
    """
    View for all data related to Movie objects.
    """

    def get(self, request):
        """
        Returns all the registered movies.
        """
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Allows to register a new movie.
        """
        serializer = MovieSerializer(data=request.data)
        message = 'Oops, something went wrong!'
        response_data = None
        if serializer.is_valid():
            serializer.save()
            message = 'Entry saved!'
            response_data = request.data
        return Response({"message": message, "data": response_data})