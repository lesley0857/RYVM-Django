"""
URL configuration for Ryvm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    
)
from clergy.views import clergy_view
from adverticements.views import advert_view
from socities.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('administration/', admin.site.urls),
    path('api/clergy/',clergy_view.as_view(), name='clergy_view'),
    path('api/adverts/',advert_view.as_view(), name='adverts_view'),
    path('api/user/', include('userapp.user_url',namespace='user_api')),
    path('api/prayer/', include('prayer.prayer_url',namespace='prayer_api')),
    path('api/society/<str:soc>/',society.as_view(),name='society_detail'),
    path('api/society/', include('socities.Society_url',namespace='society_api')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

   # urlpatterns += staticfiles_urlpatterns()
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Ss.M.R.G.C.C. Youth Site Administration"
admin.site.index_title = "Youth Site Database"
admin.site.site_title  = "Archangel Youth Site"
admin.site.login_template = "admin/login.html"
