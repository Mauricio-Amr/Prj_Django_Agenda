from django.contrib import admin
from .models import Categoria, Contato
from contatos import models


# Register your models here.
# admin.site.register(Categoria)
@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = 'id',


@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'telefone', 'show',
    ordering = 'id', 'nome', 'sobrenome'
    # list_filter = 'nome', 'data_criacao'
    search_fields = 'nome', 'sobrenome', 'telefone'
    list_per_page = 20
    list_max_show_all = 100
    list_editable = 'nome', 'sobrenome', 'show', 'telefone'
    list_display_links = 'id',
