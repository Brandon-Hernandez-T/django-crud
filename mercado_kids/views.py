from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import ClientePapa, ClienteNino
from .serializers import ClientePapaSerializer, ClienteNinoSerializer


class ClientePapaView(viewsets.ModelViewSet):
    serializer_class = ClientePapaSerializer
    queryset = ClientePapa.objects.all()


class ClienteNinoView (viewsets.ModelViewSet):
    serializer_class = ClienteNinoSerializer
    queryset = ClienteNino.objects.all()


class ClientePapaByName(generics.ListAPIView):
    serializer_class = ClientePapaSerializer
    
    def get_queryset(self):
        nombre = self.request.query_params.get('nombre')
        return ClientePapa.objects.filter(nombre__iexact=nombre)
