from rest_framework import serializers
from .models import companies


class companiesserializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:     
     model=companies
     fields="__all__"
    