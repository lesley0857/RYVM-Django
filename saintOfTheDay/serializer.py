from .models import Saint
from rest_framework import serializers


class Saints_serializer(serializers.ModelSerializer):
    class Meta:

        model = Saint
        fields = '__all__'
