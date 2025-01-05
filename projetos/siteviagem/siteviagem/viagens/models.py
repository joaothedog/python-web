from django.db import models

class Viagem(models.Model):
    DESTINOS = [
        ('Salvador', 'Salvador - R$200,00'),
        ('Vitória da Conquista', 'Vitória da Conquista - R$75,00'),
    ]
    
    motorista_whatsapp = models.CharField(max_length=15, blank=True, null=True)
    destino = models.CharField(max_length=50, choices=DESTINOS)
    nome_motorista = models.CharField(max_length=40, null=False, default='')
    horario = models.DateTimeField()
    total_passageiros = models.PositiveIntegerField(default=0)
    total_gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    excluida = models.BooleanField(default=False)
    
    @property
    def receita_bruta(self):
        precos_destinos = {
            'Salvador': 200.00,
            'Vitória da Conquista': 75.00,
        }
        return precos_destinos[self.destino] * self.total_passageiros

    @property
    def receita_liquida(self):
        total_gastos_extras = sum(gasto.valor for gasto in self.gastos_extras.all())
        return float(self.receita_bruta) - (float(self.total_gastos) + float(total_gastos_extras))

    def __str__(self):
        return f'{self.get_destino_display()} - {self.horario}'

class Passageiro(models.Model):
    nome = models.CharField(max_length=100)
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE)
    
class GastoExtra(models.Model):
    descricao = models.TextField(null=False, default='Gastos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='gastos_extras')
    
    def __str__(self):
        return f'{self.descricao} - R${self.valor}'
