from __future__ import unicode_literals

from django.db import models

class StockItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_count = models.PositiveIntegerField()
    unit_cost = models.DecimalField(max_digits=17, decimal_places=2)