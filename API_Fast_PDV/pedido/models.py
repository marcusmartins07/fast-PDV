from django.db import models
from usuarios.models import Cliente, Genero, Estado
from produto.models import Produto, Categoria

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)  
    status = models.CharField(max_length=10, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo')

    class Meta:
        abstract = True

class FormaPagamento(Base):
    forma_pagamento_id = models.AutoField(primary_key=True)
    descricao_forma = models.CharField(max_length=55)
    numero_parcela = models.IntegerField()
    
    def __str__(self):
        return self.forma_pagamento_id
    
class ClientePedido(Base):
    cliente_pedido_id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.RESTRICT)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=55)
    cidade = models.CharField(max_length=55)
    uf_estado = models.ForeignKey(Estado, on_delete=models.RESTRICT)
    email = models.EmailField(blank=True, null=True)
    tel_celular = models.CharField(max_length=12)

    def __str__(self):
        return self.cliente_pedido_id
    

class Pedido(Base):
    pedido_id = models.AutoField(primary_key=True)
    cliente_pedido_id = models.ForeignKey(ClientePedido, on_delete=models.RESTRICT, null=True, blank=True)
    valor_total_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_total_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    json_pedido = models.JSONField(default=dict)

    def __str__(self):
        return str(self.pedido_id)

class FormaPagamentoPedido(Base):
    forma_pagamento_pedido_id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    forma_pagamento_id = models.ForeignKey(FormaPagamento, on_delete=models.RESTRICT)
    descricao_forma = models.CharField(max_length=55)
    numero_parcela = models.IntegerField()
    valor_forma = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    troco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.forma_pagamento_pedido_id


class ProdutoPedido(Base):
    produto_pedido_id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    produto_id = models.ForeignKey(Produto, on_delete=models.RESTRICT)
    quantidade = models.IntegerField(default=1)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True) 
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preco_desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    porcentagem_desconto = models.IntegerField(null=True, blank=True)
    codigo_barras = models.CharField(max_length=13, blank=True)
    estoque = models.IntegerField(default=0)
    sku = models.CharField(max_length=50, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.produto_pedido_id