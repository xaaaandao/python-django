from django.db import models

# Create your models here.

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero

class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome

# OneToOne Field
# Cada carro só pode ter relacionamento com um chassi (um pra um)
# E cada chassi só pode se relacionar com um carro
# from core.models import Carro
# carros = Carro.objects.all()
# carro = Carro.objects.get(pk=1)
# Recupera o chassi
# chassi = carro.chassi
# O contrário também vale e é assim:
# from core.models import Chassi
# chassi = Chassi.objects.get(id=2)
# carro = chassi.carro

# Foreign Key (One to Many)
# Cada carro tem uma montadora, mas uma montadora pode montar vários carros
# Sempre que tiver QuerySet -> você pode pegar o first ou último dele
# Somente importando carro
# honda = fit.montadora
# R: print de honda é Honda
# Carros da montadora
# from core.models import Montadora
# honda = Montadora.objects.get(pk=1)
# carros = honda.carro_set.all()
class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE, blank=True)
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'