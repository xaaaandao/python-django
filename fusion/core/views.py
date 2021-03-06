from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation
from .models import Servico, Funcionario, Feature
from .forms import ContatoForm

# Create your views here.

# Isso chama Class Based View
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    # Depois de mandando o formulário vai para o index
    success_url = reverse_lazy('index')

    # Aqui se faz um Override
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Pega a língua do navegador
        lang = translation.get_language()
        # ? -> ordena por qualquer campo
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features'] = Feature.objects.order_by('?').all()
        context['lang'] = lang
        translation.activate(lang)
        return context

    # Se o formulário for válido envia e-mail
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # Se o formulário não for válido não envia e-mail
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
'''
Somente para o teste 400, 500
class TesteView(TemplateView):
    template_name = '500.html'
'''
