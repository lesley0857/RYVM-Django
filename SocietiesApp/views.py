from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *

# Create your views here.

class society(APIView,):
    def get(self,request,pk):
        print(pk)
        qs = Societies.objects.get(Society_name=pk)
        serialized_data = Society_serializer(qs)
        return Response(serialized_data.data)
