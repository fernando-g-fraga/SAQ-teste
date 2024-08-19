from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication

from livros.models import Livros,Retirada,Leitores
from livros.serializer import LivrosSerializer,LeitoresSerializer,RetiradaSerializer

class LivrosViewset(viewsets.ModelViewSet):
    queryset = Livros.objects.all().order_by('id')
    serializer_class = LivrosSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    
class LeitoresViewset(viewsets.ModelViewSet):
    queryset = Leitores.objects.all().order_by('id')
    serializer_class = LeitoresSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

class RetiradaViewset(viewsets.ModelViewSet):
    queryset = Retirada.objects.all().order_by('id')
    serializer_class = RetiradaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

# Create your views here.
