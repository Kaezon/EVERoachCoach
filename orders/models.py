from __future__ import unicode_literals

from django.db import models
from stock.models import StockItem

class Order(models.Model):
    customer_name = models.CharField(max_length=64)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    item_quantity = models.PositiveIntegerField()
    order_price = models.DecimalField(max_digits=17, decimal_places=2)