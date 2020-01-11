from django.views.generic import TemplateView
from .models import Servico, Funcionario, Feature

# Create your views here.

# Isso chama Class Based View
class IndexView(TemplateView):
    template_name = 'index.html'

    # Aqui se faz um Override
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # ? -> ordena por qualquer campo
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features'] = Feature.objects.order_by('?').all()
        return context

'''
Somente para o teste 400, 500
class TesteView(TemplateView):
    template_name = '500.html'
'''
