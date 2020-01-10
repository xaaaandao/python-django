from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto

# Create your views here.
# Views são sempre criadas na aplicação não no projeto
# Que é uma função Python

# É a página principal
def index(request):
    '''
    Imprime a requisição
    print(request)
    Imprime alguns parametros da requisição
    print(dir(request))
    Imprime o valor do parâmetro da requisição
    print(request.method)
    AnonymousUser -> significa que o usuário não está logado no sistema
    Quando acessa o admin você consegue o nome de usuário
    print(request.user)
    '''
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programaçaõ Web com Django Framework',
        'logado': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

'''
#Se você usar django shell, você consegue adicionar as coisas no BD, como no exemplo: 
from core.views import index
dir(index)
produto = Produto(nome="Atari 2600", preco=199.56, estoque=120)
produto.save()
# Mostra o valor de chave primária
produto.pk 

from core.models import Cliente
cliente = Cliente(cliente="Angelina", sobrenome='Jolie", email='angelina@gmail.com')
cliente.save()
# Mostra o valor de chave primária
produto.pk 

# Para alterar
cliente.nome = 'Maria'
cliente.save()

# Para deletar
cliente.delete()
'''

def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    # Para evitar que o usuário acesse um produto que num existe
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
