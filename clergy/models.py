from django.db import models
from django.utils import timezone

# Create your models here.

class Clergy(models.Model):
    clergy_name = models.CharField(max_length=150,blank=False)
    clergy_detail =  models.TextField(blank=True)
    joined_date = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(upload_to='images', default="/variac.jpeg/", blank=True, null=True)

    def __str__(self) -> str:
        return self.clergy_name