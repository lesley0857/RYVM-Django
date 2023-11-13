from django.urls import path
from.views import *

app_name = 'prayer_api'

urlpatterns=[
    path('all_prayer/',all_prayers.as_view(),name='all_prayer'),
    path('download_prayer/<int:id>/',downloadd.as_view(),name='download_prayer'),
]