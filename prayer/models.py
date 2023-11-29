from django.db import models
from socities.models import *

# Create your models here.


class Prayers(models.Model):
    name_of_prayer = models.CharField(max_length=300,null=False,blank=False)
    days = models.CharField(max_length=300,null=False,blank=False)
    society = models.ForeignKey(Societies,on_delete=models.CASCADE,null=True,blank=True,related_name='prayer_soc')
    prayer_download = models.FileField(upload_to='prayers', blank=False, null=True)

    def __str__(self):
        return f'{self.name_of_prayer}--{self.society.Society_name}'