from django.shortcuts import render, redirect
from .models import Service
from .forms import AgendamentoForm # Adicione essa importação

def home(request):
    servicos = Service.objects.all()
    return render(request, 'index.html', {'servicos': servicos})

def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AgendamentoForm()
    return render(request, 'agendar.html', {'form': form})

# Create your views here.
