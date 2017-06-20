from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Fund(models.Model):
    fund_name = models.CharField(max_length=200)
    stock_name = models.CharField(max_length=300)
    slug_url = models.SlugField(default="update_me")
    stock_allocation = models.FloatField(default=0.0)
    cash_allocation = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        self.slug_url = slugify(self.fund_name)
        super(Fund, self).save(*args, **kwargs)
    
class Stock(models.Model):
    stock_name = models.CharField(max_length=300)    
    stock_code = models.CharField(max_length=50)
