from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'servico', 'data_hora']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
        }