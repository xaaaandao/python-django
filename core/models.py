from django.db import models

# Create your models here.
# Nosso modelo de dados para virar migration

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em estoque')

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Nome', max_length=100)
    email = models.CharField('Nome', max_length=100)
