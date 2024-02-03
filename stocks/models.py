from django.db import models

class Stocks(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    ticker = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    
class StockPrice(models.Model):
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ['stock', 'date']
    
    def __str__(self):
        return f"{self.stock.name} - {self.date} - ${self.price}"