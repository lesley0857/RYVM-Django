from django.contrib import admin
from django.http.request import HttpRequest
# Register your models here.
from .models import Societies

admin.site.register(Societies)