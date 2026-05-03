from django.contrib import admin
from django.urls import path
from core.views import index, painel, agendar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('painel/', painel, name='painel'),
    path('agendar/', agendar, name='agendar'),
]