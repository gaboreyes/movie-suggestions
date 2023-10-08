from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(APIView):
    """
    foo placeholder
    """
    def get(self, request):
        """
        foo
        """
        valid_urls = {
            "users": 1,
            "movies": 2, 
            "api": 3 
        }
        return Response(valid_urls)