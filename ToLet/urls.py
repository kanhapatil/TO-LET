"""ToLet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AddFlat.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('ownersignup/', OwnerSignup, name="ownersignup"),
    path('ownerlogin/', OwnerLogin, name="ownerlogin"),
    path('ownerdashboard/', OwnerDashBoard, name="ownerdashboard"),
    path('Logout/', Logout, name="Logout"),
    path('addflats/', Add_Flat, name="addflats"),
    path('deleteflat/<int:pid>', DeleteFlat, name="deleteflat"),
    path('editflat/<int:pid>', EditFlat, name="editflat"),
    path('viewflat/<int:pid>', ViewFlat, name="viewflat"),

    # Path's for user
    path('usersignup/', UserSignup, name="usersignup"),
    path('userlogin/', UserLogin, name="userlogin"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
