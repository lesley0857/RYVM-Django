from .models import *
from .serializer import Saints_serializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class saint_view(APIView,):
    def get(self, request):
        qs = Saint.objects.all()
        serialized_data = Saints_serializer(qs, many=True)
        return Response(serialized_data.data)
