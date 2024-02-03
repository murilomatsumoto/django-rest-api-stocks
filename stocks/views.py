from rest_framework import generics
from stocks.models import Stocks, StockPrice
from stocks.serializers import StocksSerializer, StockPriceSerializer
from django.shortcuts import get_object_or_404


class StocksCreateListView(generics.ListCreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    
    
class StocksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    
    def get_object(self):
        queryset = self.get_queryset()
        ticker = self.kwargs['ticker']  # Supondo que o parâmetro na URL seja chamado 'ticker'
        obj = get_object_or_404(queryset, ticker=ticker)
        return obj
    

class StockPriceCreateListView(generics.ListCreateAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer


class StockPriceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer
    
    def get_object(self):
        queryset = self.get_queryset()
        stock_id = self.kwargs['stock_id']
        date = self.kwargs['date']
        obj = get_object_or_404(queryset, stock__id=stock_id, date=date)
        return obj