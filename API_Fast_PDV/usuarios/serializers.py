from rest_framework import serializers
from .models import Cliente, Estado, Genero
from django.contrib.auth.models import User

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'cliente_id',
            'cpf',
            'nome',
            'data_nascimento',
            'genero',
            'cep',
            'endereco',
            'numero',
            'bairro',
            'cidade',
            'uf_estado',
            'email',
            'tel_celular',
            'criacao',
            'atualizacao',
            'ativo'
        )

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = (
            'uf',
            'estado'
        )

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = (
            'id_genero',
            'genero'
        )

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )