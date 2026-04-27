from django.shortcuts import render, redirect
from .models import Service, Cliente

def index(request):
    servicos = Service.objects.all()
    return render(request, 'index.html', {'servicos': servicos})

# ... abaixo seguem as outras funções (cadastrar_servico, cadastrar_cliente, etc)

# CONFIRA SE ESTES NOMES ESTÃO ASSIM:
def cadastrar_servico(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        Service.objects.create(nome=nome, preco=preco)
    return redirect('index')

def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        Cliente.objects.create(nome=nome, telefone=telefone)
    return redirect('index')

def agendar(request):
    return render(request, 'agendar.html')

# Create your views here.
