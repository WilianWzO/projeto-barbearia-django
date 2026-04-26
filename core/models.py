from django.db import models
from django.core.exceptions import ValidationError # Importação necessária para o erro

class Service(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('C', 'Confirmado'),
        ('F', 'Finalizado'),
        ('X', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Service, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    # REGRA DE NEGÓCIO: Evitar choque de horário
    def clean(self):
        # Verifica se já existe agendamento no mesmo horário (excluindo o próprio se for edição)
        horario_ocupado = Agendamento.objects.filter(data_hora=self.data_hora).exclude(id=self.id).exists()
        
        if horario_ocupado:
            raise ValidationError('Ops! Este horário já está reservado por outro cliente. Escolha outro.')

    # Força o Django a rodar o 'clean' antes de salvar no banco
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente} - {self.servico} ({self.data_hora})"

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"