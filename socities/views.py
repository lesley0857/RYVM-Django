from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *


# Create your views here.
class all_society (APIView):
    queryset = Societies.objects.select_related('')


class society(APIView,):
    def get(self, request, soc):
        qs = Societies.objects.get(Society_name=soc)
        serialized_data = Society_serializer(qs)
        return Response(serialized_data.data)
