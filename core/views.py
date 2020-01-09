from django.shortcuts import render

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
    context = {
        'curso': 'Programaçaõ Web com Django Framework',
        'logado': teste
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

