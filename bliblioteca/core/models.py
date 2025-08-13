from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_admissao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_retirada = models.DateField(default=timezone.now)
    def get_data_devolucao_prevista():
        return timezone.now().date() + timedelta(days=7)

    data_devolucao_prevista = models.DateField(default=get_data_devolucao_prevista)
    data_devolucao_real = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.cliente} - {self.livro}"

    @property
    def atrasado(self):
        """Retorna True se a devolução estiver atrasada"""
        if self.data_devolucao_real:
            return self.data_devolucao_real > self.data_devolucao_prevista
        return timezone.now().date() > self.data_devolucao_prevista

    @property
    def multa(self):
        """Calcula a multa com base nos dias de atraso (R$ 2,00/dia)"""
        if self.atrasado:
            fim = self.data_devolucao_real or timezone.now().date()
            dias_atraso = (fim - self.data_devolucao_prevista).days
            return dias_atraso * 2.00
        return 0.0
