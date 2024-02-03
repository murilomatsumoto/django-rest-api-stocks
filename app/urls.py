from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from stocks.views import StocksCreateListView, StocksRetrieveUpdateDestroyView, StockPriceCreateListView, StockPriceRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('stocks/', StocksCreateListView.as_view(), name = 'stocks-create-list'),
    path('stocks/<int:pk>/', StocksRetrieveUpdateDestroyView.as_view(), name = 'stocks-datail-view'),
    path('stockprices/', StockPriceCreateListView.as_view(), name='stockprices-list-create'),
    path('stockprices/<int:pk>/', StockPriceRetrieveUpdateDestroyView.as_view(), name='stockprices-retrieve-update-destroy'),
]
