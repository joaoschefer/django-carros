from django.contrib import admin
from .models import Carro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'cor', 'quilometragem', 'data_criacao')
    search_fields = ('marca', 'modelo', 'ano', 'cor')
    list_filter = ('marca', 'ano', 'cor')