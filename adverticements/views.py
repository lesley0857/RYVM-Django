from django.shortcuts import render
from .models import Adverts
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Adverts
from .serializer import Adverts_serializer

class advert_view(APIView,):
    def get(self,request):
        qs = Adverts.objects.all()
        serialized_data = Adverts_serializer(qs,many=True)
        return Response(serialized_data.data)