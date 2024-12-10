from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Cliente, Estado, Genero
from .serializers import ClienteSerializer, EstadoSerializer, GeneroSerializer, UsuariosSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth
from django.contrib.auth.models import User
from .bd_backup import insert_bd
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password


import time
import random

class CustomPagination(PageNumberPagination):
    page_size = 27
    page_size_query_param = 'page_size' 



class ClienteViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=False, methods=['get'])
    def buscar_por_cpf(self, request):
        cpf = request.query_params.get('cpf', None)
        if cpf:
            try:
                clienteResponse = self.queryset.get(cpf=cpf)
                serializer = self.get_serializer(clienteResponse)
                return Response(serializer.data)
            except Cliente.DoesNotExist:
                return Response({"detail": "Cliente não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "CPF inválido ou não fornecido."}, status=status.HTTP_400_BAD_REQUEST)
    
class EstadoViewSet(mixins.ListModelMixin, 
                     viewsets.GenericViewSet):
    queryset = Estado.objects.all().order_by('uf')
    #insert_bd()
    serializer_class = EstadoSerializer
    pagination_class = CustomPagination
    

class GeneroViewSet(mixins.ListModelMixin, 
                     viewsets.GenericViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    pagination_class = CustomPagination

class UsuariosViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], url_path='validar-senha')
    def validar_senha(self, request):
        senha = request.data.get('senha', None)
        if not senha:
            return Response({'error': 'O campo senha é obrigatório.'}, status=400)

        usuario = request.user

        if check_password(senha, usuario.password):
            return Response({'message': 'Senha válida'}, status=200)
        return Response({'error': 'Senha inválida'}, status=400)
