from django.urls import path
from.views import *

app_name = 'society_api'

urlpatterns=[
path('<str:pk>/',society.as_view(),name='society_detail'),
]