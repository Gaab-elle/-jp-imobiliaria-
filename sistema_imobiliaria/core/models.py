from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Residencial com vários apartamentos
class Residencial(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

# Cada apartamento pertence a um residencial
class Apartamento(models.Model):
    residencial = models.ForeignKey(Residencial, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    bloco = models.CharField(max_length=10, blank=True, null=True)
    metragem = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ocupado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.residencial.nome} - Apto {self.numero}"

# Moradores associados a apartamentos
class Morador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.SET_NULL, null=True, blank=True)
    bom_pagador = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

# Contrato com início e fim
class Contrato(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Contrato de {self.morador.nome}"

# Chamado de manutenção
class Manutencao(models.Model):
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_abertura = models.DateField(auto_now_add=True)
    resolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"Manutenção - {self.apartamento}"

# Histórico de pagamentos
class Pagamento(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    pago = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.morador.nome} - {self.data_pagamento}"
