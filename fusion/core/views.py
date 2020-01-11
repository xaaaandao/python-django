from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

'''
class TesteView(TemplateView):
    template_name = '500.html'
'''
