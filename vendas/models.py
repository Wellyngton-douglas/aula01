from django.db import models

# Create your models here.

class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    data_venda = models.DateField(auto_now_add=True, null= False, blank=True)
    hora_venda = models.TimeField(auto_now_add=True, null= False, blank=True)
    data_hora_venda =models.DateTimeField(auto_now_add=True, null= False, blank=True)
    numero_venda = models.IntegerField(null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    comprovante_venda = models.FileField(upload_to='comprovante_venda/')
    email_cliente = models.EmailField(null=True, blank=True)
    venda_concluida = models.BooleanField(null=False, blank=False)
    qtd_itens = models.IntegerField(null=False, blank=True, default=0)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome