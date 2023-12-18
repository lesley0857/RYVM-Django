from rest_framework import serializers
from .models import AnnoncementModel


class AnnouncementSerilizer(serializers.ModelSerializer):
    class Meta:
        model = AnnoncementModel
        fields = '__all__'
