from rest_framework import serializers
from .models import ClientePapa, ClienteNino

class ClientePapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientePapa
        fields = '__all__'

class ClienteNinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteNino
        fields = '__all__'
