from django.shortcuts import render
from .models import companies
from rest_framework import serializers, viewsets
from .serializers import companiesserializer

# Create your views here.


class companiesviewset(viewsets.ModelViewSet):
    queryset=companies.objects.all()
    serializer_class=companiesserializer