from rest_framework import generics
from stocks.models import Stocks, StockPrice
from stocks.serializers import StocksSerializer, StockPriceSerializer


class StocksCreateListView(generics.ListCreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    
    
class StocksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    

class StockPriceCreateListView(generics.ListCreateAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer


class StockPriceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer