from django import forms
from django.forms import ModelForm
from models import StockItem

class AddItemForm(ModelForm):
    class Meta:
        model = StockItem
        fields = '__all__'

class AddStockForm(ModelForm):
    class Meta:
        model = StockItem
        fields = ['item_count','unit_cost']