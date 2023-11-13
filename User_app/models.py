from typing import Any
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import (pre_save, post_save)
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from SocietiesApp.models import Societies


# Create your models here.

class RYVM_user_Manager(BaseUserManager):
    def create_user(self,email,firstname,lastname,password=None):
        if firstname is None:
            raise ValueError('User should have a username')
        if lastname is None:
            raise ValueError('Please fill lastname')
        if email is None:
            raise ValueError(_('Please provide an email'))
        email = self.normalize_email(email)
        user= self.model(email=email,firstname=firstname,lastname=lastname)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,firstname,lastname,password=None):

        user  =  self.create_user(email,firstname,lastname,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
        


class Custom_Base_User(AbstractBaseUser,PermissionsMixin):
    STATUS = (('Single','Single'),('Married','Married'),('Widowed','Widowed'))
    email= models.EmailField(_('email address'), unique=True)
    firstname = models.CharField(max_length=150,blank=False)
    lastname = models.CharField(max_length=150,blank=False)
    joined_date = models.DateTimeField(default=timezone.now)
    phone_number = models.PositiveIntegerField( blank=False,null=True)
    alternative_number = models.PositiveIntegerField( blank=True,null=True)
    marital_status = models.CharField(max_length=200,choices=STATUS,default= 'PLANS[0]',blank=False,null=True)
    next_of_kin = models.CharField(max_length=150,blank=False, default="Nulll")
    next_of_kin_number = models.PositiveIntegerField(blank=False,null=True)
    profile_pic = models.ImageField(upload_to='images', default="/variac.jpeg/", blank=True, null=True)
    about_user =  models.TextField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    
    objects = RYVM_user_Manager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname']

    def __str__(self):
        return f'{self.lastname}:{self.firstname}'
    


class User_Socities(models.Model):
    user = models.ForeignKey(Custom_Base_User,on_delete=models.SET_NULL,null=True,blank=False)
    society = models.ForeignKey(Societies,on_delete=models.SET_NULL,null=True, blank=False)
    
    def __str__(self):
        return f'{self.user} in {self.society}'
    
    def save(self):
        try:
            user= User_Socities.objects.filter(user__id=self.user.id,society__id=self.society.id)
            if user.count() >= 1:
                print('more than one')
                
            else:
                super(User_Socities,self).save()
        except:
            super(User_Socities,self).save()
            






    
