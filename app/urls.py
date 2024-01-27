from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from stocks.views import StocksCreateListView, StocksRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('stocks/', StocksCreateListView.as_view(), name = 'stocks-create-list'),
    path('stocks/<int:pk>/', StocksRetrieveUpdateDestroyView.as_view(), name = 'stocks-datail-view'),
]
