from .models import Clergy
from rest_framework import serializers


class Clergy_serializer(serializers.ModelSerializer):
    class Meta:
        
        model=Clergy
        fields='__all__'