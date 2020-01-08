from django.contrib import admin

# Register your models here.
# Para criar um novo admin python manage.py createsuperuser

from .models import Produto, Cliente

# Para aparecer informações de nome, preço e quantidade de estoque
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

# Para aparecer esses modelos lá
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
