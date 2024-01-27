from django.db import models

class Stocks(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name