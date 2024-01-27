from rest_framework import generics
from stocks.models import Stocks
from stocks.serializers import StocksSerializer


class StocksCreateListView(generics.ListCreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    
    
class StocksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer