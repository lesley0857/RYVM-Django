from django.db import models
from userapp.models import Custombaseuser
# Create your models here.


class PaymentModel(models.Model):
    user = models.ForeignKey(
        Custombaseuser, models.SET_NULL, null=True, blank=False)
    reference_id = models.CharField(max_length=150, blank=False)
    amount = models.IntegerField(blank=False)
    description = models.TextField(max_length=150, blank=False)
    firstName = models.CharField(max_length=150, blank=False)
    time = models.DateTimeField(auto_now_add=True, null=True)
    lastName = models.CharField(max_length=150, blank=False)
    other_fields = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.email}---N{self.amount} BY {self.time}'
