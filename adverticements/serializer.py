from rest_framework import serializers
from .models import Adverts

class Adverts_serializer(serializers.ModelSerializer):
    class Meta:
        model=Adverts
        fields='__all__'