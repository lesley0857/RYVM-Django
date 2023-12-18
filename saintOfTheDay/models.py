from django.db import models

# Create your models here.


class Saint(models.Model):
    name_of_saint = models.CharField(max_length=150, blank=False)
    life_of_saint = models.TextField(blank=True)
    joined_date = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(
        upload_to='images', default="/variac.jpeg/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name_of_saint
