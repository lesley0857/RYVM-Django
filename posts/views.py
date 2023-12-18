from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import AnnoncementModel
from . serializer import AnnouncementSerilizer

# Create your views here.


class AnnouncementView(APIView):
    def get(self, request):
        all = AnnoncementModel.objects.all()
        announcement = AnnouncementSerilizer(insatnce=all)
        return Response({'announcement': announcement}, status=status.HTTP_200_OK)
