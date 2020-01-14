from django.db import models
from django.contrib.auth import get_user_model

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

def set_default_montadora():
    # Cria uma montadora Padrão
    return Montadora.objects.get_or_create(nome='Padrão')[0] # Retorna um objeto e boolean

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

# (Many to Many)
# Um carro pode ser dirigido por vários motoristas e um
# motorista pode dirigir diversos carros
# from core.models import Carro
# carros = Carro.objects.all()
# carro1 = carros.first()
# mostra todos motoristas
# motos1 = carro1.motoristas.all()
# carro2 = carros.last()
# motos2 = carro2.motoristas.all()
# todos os carros que essa lista dirige
# m1 = motos1.first()
# carros = Carro.objects.filter(motoristas=m1)
# carro que os dois motoristas dirigem, isso pq eh uma lista
# carros = Carro.objects.filter(motoristas__in = motos1).distinct()
class Carro(models.Model):
    # Letras maiuscúlas são CONSTANTES
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    # Se apagar set como default o que é 1
    # montadora = models.ForeignKey(Montadora, on_delete=models.SET_DEFAULT, default=1)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE, blank=True)
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'