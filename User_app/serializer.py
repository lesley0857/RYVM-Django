from .models import Custom_Base_User,User_Socities
from rest_framework import serializers
from SocietiesApp.views import *
from Ryvm_project.urls import *

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_Base_User
        fields = ['firstname','lastname','email',
                  'phone_number','alternative_number',
                  'marital_status','next_of_kin',
                  'next_of_kin_number',
                  'profile_pic','password',]
       # extra_kwargs = {'password',{'write_only':True}}
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class User_details_Serilizer(serializers.ModelSerializer):
    class Meta:
        model = Custom_Base_User
        fields = '__all__'

class User_Society_serializer(serializers.ModelSerializer):
    #society=serializers.HyperlinkedRelatedField(view_name="society_detail",read_only=True)
    society=serializers.StringRelatedField()
    
    class Meta:
        model=User_Socities
        fields='__all__'




