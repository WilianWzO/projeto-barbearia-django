from django.shortcuts import render, redirect
from .models import Servico, Cliente, Agendamento

def get_textos(lang):
    """Dicionário central de traduções"""
    textos = {
        'en': {
            'titulo': 'BARBER SHOP', 'agendar': 'BOOK NOW', 'gestao': 'MANAGEMENT', 
            'busca': 'Search...', 'voltar': 'BACK TO SITE', 'exclusivo': 'Exclusive', 
            'slogan': 'Cut for every Style', 'servicos': 'SERVICES', 'clientes': 'CLIENTS',
            'salvar': 'SAVE', 'editar': 'EDIT', 'confirmar': 'CONFIRM',
            'data_hora': 'DATE AND TIME'
        },
        'es': {
            'titulo': 'BARBER SHOP', 'agendar': 'RESERVAR', 'gestao': 'GESTIÓN', 
            'busca': 'Buscar...', 'voltar': 'VOLVER AL SITIO', 'exclusivo': 'Exclusivo', 
            'slogan': 'Corte para cada Estilo', 'servicos': 'SERVICIOS', 'clientes': 'CLIENTES',
            'salvar': 'GUARDAR', 'editar': 'EDITAR', 'confirmar': 'CONFIRMAR',
            'data_hora': 'FECHA Y HORA'
        },
        'pt-br': {
            'titulo': 'BARBER SHOP', 'agendar': 'AGENDAR AGORA', 'gestao': 'GESTÃO', 
            'busca': 'Busca...', 'voltar': 'VOLTAR AO SITE', 'exclusivo': 'Exclusivo', 
            'slogan': 'Corte para cada Estilo', 'servicos': 'SERVIÇOS', 'clientes': 'CLIENTES',
            'salvar': 'SALVAR', 'editar': 'EDITAR', 'confirmar': 'CONFIRMAR',
            'data_hora': 'DATA E HORÁRIO'
        }
    }
    return textos.get(lang, textos['pt-br'])

def index(request):
    if request.method == 'POST' and 'language' in request.POST:
        request.session['django_language'] = request.POST.get('language')
        return redirect('index')
    lang = request.session.get('django_language', 'pt-br')
    return render(request, 'index.html', {'servicos': Servico.objects.all(), 't': get_textos(lang)})

def painel(request):
    lang = request.session.get('django_language', 'pt-br')
    servico_edit = Servico.objects.filter(id=request.GET.get('edit_servico')).first()
    cliente_edit = Cliente.objects.filter(id=request.GET.get('edit_cliente')).first()

    if request.method == 'POST':
        tipo, item_id = request.POST.get('form_type'), request.POST.get('item_id')
        if tipo == 'servico':
            n, p = request.POST.get('nome'), request.POST.get('preco')
            if item_id:
                s = Servico.objects.get(id=item_id); s.nome, s.preco = n, p; s.save()
            else: Servico.objects.create(nome=n, preco=p)
        elif tipo == 'cliente':
            n = request.POST.get('nome')
            if item_id:
                c = Cliente.objects.get(id=item_id); c.nome = n; c.save()
            else: Cliente.objects.create(nome=n)
        elif tipo == 'delete_servico':
            Servico.objects.get(id=item_id).delete()
        elif tipo == 'delete_cliente':
            Cliente.objects.get(id=item_id).delete()
        return redirect('painel')

    return render(request, 'painel.html', {
        'servicos': Servico.objects.all(), 'clientes': Cliente.objects.all(), 
        'servico_edit': servico_edit, 'cliente_edit': cliente_edit, 't': get_textos(lang)
    })

def agendar(request):
    lang = request.session.get('django_language', 'pt-br')
    servico_id_get = request.GET.get('servico_id')
    
    if request.method == 'POST':
        c_id = request.POST.get('cliente')
        s_id = request.POST.get('servico')
        data_agendamento = request.POST.get('data')

        if c_id and s_id and data_agendamento:
            # Trava para não deixar dois clientes no mesmo horário
            if Agendamento.objects.filter(data=data_agendamento).exists():
                return render(request, 'agendar.html', {
                    'servicos': Servico.objects.all(), 
                    'clientes': Cliente.objects.all(), 
                    'erro': "HORÁRIO OCUPADO!", 
                    't': get_textos(lang)
                })
            
            Agendamento.objects.create(
                cliente=Cliente.objects.get(id=c_id),
                servico=Servico.objects.get(id=s_id),
                data=data_agendamento
            )
            return redirect('index')

    return render(request, 'agendar.html', {
        'servicos': Servico.objects.all(), 
        'clientes': Cliente.objects.all(), 
        'servico_selecionado_id': servico_id_get, 
        't': get_textos(lang)
    })