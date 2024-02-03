from django.db import models

class Stocks(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class StockPrice(models.Model):
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    date = models.DateField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.stock.name} - {self.date} - ${self.price}"