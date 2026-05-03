from django.contrib import admin
from django.urls import path, include
from core.views import index, painel, agendar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')), # Destrava as bandeiras
    path('', index, name='index'), # Destrava o botão voltar
    path('painel/', painel, name='painel'),
    path('agendar/', agendar, name='agendar'),
]