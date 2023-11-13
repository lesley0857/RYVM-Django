from .models import Prayers
from rest_framework import serializers


class Prayer_serializer(serializers.ModelSerializer):
    class Meta:
        model=Prayers
        fields='__all__'