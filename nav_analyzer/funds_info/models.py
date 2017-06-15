from django.db import models

# Create your models here.
class Fund(models.Model):
    fund_name = models.CharField(max_length=200)
    stock_name = models.CharField(max_length=300)
    
class Stock(models.Model):
    stock_name = models.CharField(max_length=300)    
    stock_code = models.CharField(max_length=50)
