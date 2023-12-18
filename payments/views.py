from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from rest_framework import status
from .models import PaymentModel
from userapp.models import Custombaseuser
from itertools import combinations

# Create your views here.


class PaymentView(APIView):
    def post(self, request):
        data = request.data
        user = Custombaseuser.objects.filter(email=data['email'])
        try:
            data['other_fields']
            other_fields = data['other_fields']
            PaymentModel.objects.create(user=user.first(),
                                        reference_id=data['reference_id'],
                                        amount=data['amount'],
                                        description=data['description'],
                                        firstName=data['firstName'],
                                        lastName=data['lastName'],
                                        other_fields=data['other_fields'])

            return Response(status=status.HTTP_201_CREATED)
        except:
            PaymentModel.objects.create(user=user.first(),
                                        reference_id=data['reference_id'],
                                        amount=data['amount'],
                                        description=data['description'],
                                        firstName=data['firstName'],
                                        lastName=data['lastName'],)

            return Response(status=status.HTTP_201_CREATED)
