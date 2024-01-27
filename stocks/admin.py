from django.contrib import admin
from stocks.models import Stocks

#alteração para adicionar registros na tabela do DB via url do admin
@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
