from django.contrib import admin

from .models import Venda, Produto, Cliente
# Register your models here.

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ("nome", "valor", "data_venda", "hora_venda")
    list_filter = ("data_venda",)
    search_fields = ("nome",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "valor")
    list_filter = ("nome",)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "email_cliente")
    search_fields = ("nome",)
