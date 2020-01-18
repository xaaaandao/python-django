from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from django.urls import reverse_lazy

# Create your views here.

class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    # É o que agente vai usar para recuperar lá no template
    context_object_name = 'produtos'

class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    # entro no formulário foi inserido com sucesso, para onde vai ser levado...
    success_url = reverse_lazy('index')

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')