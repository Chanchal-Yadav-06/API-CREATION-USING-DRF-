from django.contrib import admin
from django.urls import path,include
from .views import companiesviewset
from rest_framework import routers, viewsets, serializers 


routers=routers.DefaultRouter()
routers.register(r'companies',companiesviewset)

urlpatterns = [
    path('',include(routers.urls))
   
]