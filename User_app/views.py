from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.http import HttpRequest
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,)
from .models import Custom_Base_User,User_Socities
from .serializer import User_serializer, User_details_Serilizer,User_Society_serializer
from prayer.models import Prayers
from SocietiesApp.models import Societies
from SocietiesApp.serializer import Society_serializer
from rest_framework.parsers import MultiPartParser, FormParser



class user_detail(APIView):
    permission_classes =  (IsAuthenticated,)
    def get(self,request,email):
        user = Custom_Base_User.objects.get(email=email)
        list_of_society_pictures = []
        serializer_context = {'request': request,}
        if user:
            serialized_user = User_details_Serilizer(instance=user)
            user_societies_qs = User_Socities.objects.filter(user=user)
            user_societies = User_Society_serializer(user_societies_qs,context={'request': request},many=True)
            for i in user_societies.data:
                sc = Societies.objects.get(Society_name=i['society'])
                print(sc.profile_pic)
                list_of_society_pictures.append(sc)
                print(f'list{list_of_society_pictures}')
            qa = Society_serializer(list_of_society_pictures, many=True)
            return Response({
                            # 'Societies':user_societies.data,
                            "list_of_society_pictures":qa.data,
                             'User_datails':serialized_user.data})
        else:
            return Response({'email':'No user with such email'})


class User_create(APIView,):
    permission_classes =  [AllowAny,]
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        print(request.data)
        try:
           existing_user =  Custom_Base_User.objects.get(email=request.data['email'])
           return Response({'message:User already exists !!!!'})
        except:
            pass
        user = User_serializer(data=request.data)
        if user.is_valid(raise_exception=True):
            newuser = user.save() 
            if newuser:
                return Response({'message':'Successful'}, status=status.HTTP_201_CREATED)
        return Response(User_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  

    