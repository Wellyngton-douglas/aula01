from django.db import models

# Create your models here.

class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Codigo do contrato')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, 
        verbose_name='Valor total da venda')
    data_venda = models.DateField(auto_now_add=True, null= False, blank=True)
    hora_venda = models.TimeField(auto_now_add=True, null= False, blank=True)
    data_hora_venda =models.DateTimeField(auto_now_add=True, null= False, blank=True)
    numero_venda = models.IntegerField(null=True, blank=True, verbose_name='Número da Venda')
    observacao = models.TextField(null=True, blank=True, verbose_name='Observação')
    comprovante_venda = models.FileField(upload_to='comprovante_venda/', verbose_name='Comprovante de Venda')
    venda_concluida = models.BooleanField(null=False, blank=False)
    qtd_itens = models.IntegerField(null=False, blank=True, default=0, verbose_name='Quantidade de Itens Vendidos')
    produtos = models.ManyToManyField('Produto')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do produto')
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, verbose_name='Valor do produto')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome