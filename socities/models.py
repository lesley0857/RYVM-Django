from django.db import models

# Create your models here.
class Societies(models.Model):
    Society_name = models.CharField(max_length=300,null=False,blank=False,default="Society Name")
    Venue = models.CharField(max_length=300,null=False,blank=False,default="Church Compound")
    contact_number = models.PositiveIntegerField( blank=True,null=True)
    alternative_number = models.PositiveIntegerField( blank=True,null=True)
    Days_of_meeting = models.CharField(max_length=300,null=False,blank=False,default='Sunday')
    profile_pic = models.ImageField(default="/Koala.jpg/")

    def __str__(self):
        return f'{self.Society_name}'
    