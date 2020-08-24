from django.contrib import admin

from .models import TiposPicole, TiposEmbalagem

# Register your models here.
@admin.register(TiposEmbalagem)
class TiposEmbalagemAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(TiposPicole)
class TiposPicoleAdmin(admin.ModelAdmin):
    list_display = ('nome',)
