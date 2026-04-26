from django.contrib import admin
from .models import Service, Cliente, Agendamento

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

class AgendamentoAdmin(admin.ModelAdmin):
    # Isso cria colunas na lista principal!
    list_display = ('cliente', 'servico', 'data_hora', 'status')
    
    # Isso cria uma barra lateral de filtros (muito útil!)
    list_filter = ('status', 'data_hora', 'servico')
    
    # Isso cria uma barra de busca pelo nome do cliente
    search_fields = ('cliente__nome',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Cliente)
admin.site.register(Agendamento, AgendamentoAdmin)