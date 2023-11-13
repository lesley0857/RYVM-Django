from django.db import models
from django.utils import timezone
# Create your models here.


class Adverts(models.Model):
    adverticement_name = models.CharField(max_length=150,blank=False)
    adverticement_image = models.ImageField(upload_to='images', default="/variac.jpeg/", blank=True, null=True)

    def __str__(self) -> str:
        return self.adverticement_name