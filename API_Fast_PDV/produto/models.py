from django.db import models
from decimal import Decimal


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)  
    status = models.CharField(max_length=10, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo')

    class Meta:
        abstract = True

class Categoria(Base):
    codigo_categoria = models.CharField(max_length=4, primary_key=True)
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Produto(Base):
    produto_id = models.AutoField(primary_key=True, default=None)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True) 
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preco_desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    porcentagem_desconto = models.IntegerField(null=True, blank=True)
    codigo_barras = models.CharField(max_length=13, unique=True, blank=True)
    estoque = models.IntegerField(default=0)
    sku = models.CharField(max_length=50, unique=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)


    def save(self, *args, **kwargs):
            if self.preco_venda and self.preco_desconto:
                self.porcentagem_desconto = int(((self.preco_venda - self.preco_desconto) / self.preco_venda) * 100)
            elif self.preco_venda and self.porcentagem_desconto is not None:
                # Se a porcentagem de desconto for fornecida, calcular o preço de desconto
                if 0 <= self.porcentagem_desconto <= 100:  # Validar se a porcentagem está entre 0 e 100
                    # Converte self.porcentagem_desconto para Decimal
                    desconto_percentual = Decimal(self.porcentagem_desconto) / Decimal(100)
                    preco_com_desconto = self.preco_venda * (1 - desconto_percentual)
                    self.preco_desconto = self.preco_venda-preco_com_desconto
                else:
                    raise ValueError("Desconto porcentagem deve estar entre 0 e 100")
            else:
                self.porcentagem_desconto = None  # Ou 0, dependendo da sua lógica
                self.preco_desconto = None  # Ou 0, dependendo da sua lógica

            super().save(*args, **kwargs)