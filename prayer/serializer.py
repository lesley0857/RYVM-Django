from .models import Prayers
from rest_framework import serializers


class Prayer_serializer(serializers.ModelSerializer):
    society=serializers.StringRelatedField()
    class Meta:
        model=Prayers
        fields='__all__'