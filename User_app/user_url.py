from django.urls import path
from .views import *


app_name = 'user_api'

urlpatterns = [
    path('register_user/',User_create.as_view(), name='user_create'),
    path('user_detail/<str:email>/',user_detail.as_view(), name='user_detail'),
]