from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import Prayer_serializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.http import HttpResponse 
from .models import *
import json
import mimetypes
import os

# Create your views here.

class all_prayers(APIView):
    serializer_class = Prayer_serializer
    def get(self,request):
        prayers = Prayers.objects.select_related('society')
        print(prayers)
        a = [i for i in prayers]
        serialized_data = Prayer_serializer(instance=a, many=True)
        if serialized_data:
            return Response(serialized_data.data) 
        return Response({'email':'No user with such email'})
    
class downloadd(APIView):
    def get(self,request,id):
        try:
            file_to_download = Prayers.objects.get(id=id)
            filename = file_to_download.prayer_download
            filepath = f'{filename.path}'
            mime_type, _ = mimetypes.guess_type(filepath)
            response =  HttpResponse(file_to_download.prayer_download, content_type = mime_type)
            response['Content-Disposition']=f'attachment; {filename}'
            return response
        except:
            return Response({'message':'Not available'})
