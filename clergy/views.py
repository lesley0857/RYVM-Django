from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import Clergy_serializer

# Create your views here.

class clergy_view(APIView,):
    def get(self,request):
        qs = Clergy.objects.all()
        serialized_data = Clergy_serializer(qs,many=True)
        return Response(serialized_data.data)


