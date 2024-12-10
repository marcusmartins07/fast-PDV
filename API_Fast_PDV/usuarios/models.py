from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)  
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Genero(Base):
    id_genero = models.CharField(max_length=2, primary_key=True)
    genero = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.id_genero

class Estado(Base):
    uf = models.CharField(max_length=2, primary_key=True)
    estado = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.uf


class Cliente(Base):
    cliente_id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
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


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['cliente_id']
        unique_together = ['cpf']

    def __str__(self):
        return self.nome