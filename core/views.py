from django.shortcuts import render

# Create your views here.
# Views são sempre criadas na aplicação não no projeto
# Que é uma função Python

# É a página principal
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')