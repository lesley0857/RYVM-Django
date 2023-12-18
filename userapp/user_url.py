from django.urls import path
from .views import *


app_name = 'user_api'

urlpatterns = [
    path('register_user/', User_create.as_view(), name='user_create'),
    path('user_detail/<str:email>/', user_detail.as_view(), name='user_detail'),
    path('user_verify/<str:email>/', user_verify, name='user_verify'),
    path('reset_password_form/', reset_password_form.as_view(),
         name='reset_password_form'),

]
