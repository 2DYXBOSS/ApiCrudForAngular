from rest_framework import serializers
from monapp.models import Monmodel

class Monserialiser(serializers.ModelSerializer):
    class Meta :
        model = Monmodel
        fields = ['id','name','description']