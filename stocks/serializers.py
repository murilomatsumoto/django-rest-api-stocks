from rest_framework import serializers
from stocks.models import Stocks, StockPrice


class StocksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stocks
        fields = '__all__'

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = '__all__'