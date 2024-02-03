from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from stocks.views import StocksCreateListView, StocksRetrieveUpdateDestroyView, StockPriceCreateListView, StockPriceRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('stocks/', StocksCreateListView.as_view(), name = 'stocks-create-list'),
    path('stocks/<str:ticker>/', StocksRetrieveUpdateDestroyView.as_view(), name='stocks-retrieve-update-destroy'),
    path('stockprices/', StockPriceCreateListView.as_view(), name='stockprices-list-create'),
    path('stockprices/<int:stock_id>/<str:date>/', StockPriceRetrieveUpdateDestroyView.as_view(), name='stockprices-retrieve-update-destroy'),
    
]
