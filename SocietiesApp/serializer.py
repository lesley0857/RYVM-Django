from .models import Societies
from rest_framework import serializers

class Society_serializer(serializers.ModelSerializer):
    class Meta:
        model=Societies
        fields='__all__'