from django.shortcuts import render
from django.views.generic import ListView
from .models import Produto

# Create your views here.

class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    paginate_by = 5
    # Ordena decrescente...
    # ordering = '-id'
    ordering = 'id'

