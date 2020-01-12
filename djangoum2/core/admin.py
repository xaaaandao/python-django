from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    # remove o dropdown de autor
    exclude = ['autor',]

    # Para pegar o nome inteiro do autor
    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    # Só vê seus posts
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    # Está sobrescrevendo o model, para que ele pegue o id do autor para ser salvo
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)