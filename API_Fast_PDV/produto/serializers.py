from rest_framework import serializers
from .models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Categoria
        fields = (
            'nome',
            'codigo_categoria',  
            'status'
        )

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(slug_field='nome', queryset=Categoria.objects.all())
    class Meta:
        model = Produto
        fields = (
            'produto_id',
            'nome',
            'descricao',
            'preco_venda',
            'preco_desconto',
            'porcentagem_desconto',
            'preco_custo',
            'codigo_barras',
            'estoque',
            'sku',
            'categoria',
            'status'
        )