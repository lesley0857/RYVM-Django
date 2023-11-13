from typing import Any, List, Optional
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db.models.query import QuerySet
from django.urls.resolvers import URLPattern
from django.http.request import HttpRequest
from django.urls import path
from django.shortcuts import render
from .models import *

# Register your models here.


admin.site.register(Custom_Base_User)
admin.site.register(User_Socities)
