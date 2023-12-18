from django.shortcuts import render
import os
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import HttpRequest
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,)
from rest_framework.decorators import api_view
from .models import Custombaseuser, Usersocities
from .serializer import User_serializer, User_details_Serilizer, User_Society_serializer
from prayer.models import Prayers
from socities.models import Societies
from socities.serializer import Society_serializer
from rest_framework.parsers import MultiPartParser, FormParser
from .sql_script import sql_query
from django.contrib import admin
from clergy.models import Clergy
from django.core.mail import EmailMessage, get_connection
from django.conf import Settings
from .custom_token import Token_Customizer
from django.template.loader import render_to_string
from .tasks import *
import json
from json import JSONEncoder
import pickle
from datetime import date, timedelta


class user_detail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, email):
        # celebrants = Custombaseuser.objects.filter(birth_date=f'{date.today}')
        user = Custombaseuser.objects.get(email=email)
        print(type(user.birth_date))
        print(type(date.today()))
        usersociety = Usersocities.objects.select_related(
            'user').all().filter(user__id=user.id)
        societies_related_to_user = [i.society for i in usersociety]

        serialized_societies_related_to_user = Society_serializer(
            societies_related_to_user, many=True)
        print(serialized_societies_related_to_user.data)
        # adminn = list(map(lambda x:Usersocities.objects.filter(society__id=x.id,position='Admin') , societies_related_to_user))
        # print(adminn)
        if user:
            serialized_user = User_details_Serilizer(instance=user)
            return Response({'User_datails': serialized_user.data,
                             'Societies': serialized_societies_related_to_user.data,
                             }, status=status.HTTP_200_OK)
        else:
            return Response({'email': 'No user with such email'}, status=status.HTTP_401_UNAUTHORIZED)


class User_create(APIView,):
    permission_classes = [AllowAny,]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        print(request.data)
        try:
            existing_user = Custombaseuser.objects.get(
                email=request.data['email'])
            return Response({'message': 'User already exists !!!!'})
        except:
            pass
        user = User_serializer(data=request.data)
        if user.is_valid(raise_exception=True):
            newuser = user.save()
            token = Token_Customizer.get_token(newuser)
            serialized_token = json.dumps(str(token))
            subject = 'Verify Your Email'
            from_email = 'nwekelesley@gmail.com'
            to = newuser.email
            send_email_task.delay(
                subject, from_email, serialized_token, to)
            print('here1')
            if newuser:
                return Response({'message': 'Successful'}, status=status.HTTP_201_CREATED)

        return Response(User_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_verify(request, email):
    if request.method == 'POST':  # unncecessary
        try:
            verified_user = Custombaseuser.objects.get(
                email=request.data['email'])
            verified_user.email_verified = True
            verified_user.save()
            return Response({'message': 'Email verified'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Not verified, Please Register'}, status=status.HTTP_401_UNAUTHORIZED)


class reset_password_form(APIView,):
    permission_classes = [AllowAny,]

    def post(self, request):
        print(request.data['check'])
        if request.data['check'] == "check email for reset_password":
            print(request.data['check'])
            try:
                user = Custombaseuser.objects.get(email=request.data['email'])
                token = Token_Customizer.get_token(user)
                serialized_token = json.dumps(str(token))
                subject = 'Reset Password'
                from_email = 'nwekelesley@gmail.com'
                to = user.email
                Send_reset_password_email.delay(
                    serialized_token, subject, from_email, to)
                return Response({'message': "Valid account"})
            except:
                return Response({'message': "Invalid account"})
        elif request.data['check'] == "Reset_Password":
            try:
                user = Custombaseuser.objects.get(email=request.data['email'])
                user.set_password(request.data['password1'])
                user.save()
                return Response({'message': "Password Changed"}, status=status.HTTP_200_OK)
            except:
                return Response({'message': "Invalid Account"}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({'message': "You dont have an account"}, status=status.HTTP_400_BAD_REQUEST)
