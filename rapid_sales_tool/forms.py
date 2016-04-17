from django.forms import ModelForm, ModelChoiceField
from django.forms.models import inlineformset_factory
from .models import *

class AddItemForm(ModelForm):
    class Meta:
        model = StockItem
        fields = '__all__'

class AddStockForm(ModelForm):
    class Meta:
        model = StockItem
        fields = ['item_count','unit_cost']

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('order_price','is_paid')
    def __init__(self, *args, **kwargs):
        super(AddOrderForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = StockItem.objects.all()
        self.fields['item'].label_from_instance = lambda obj: "%s" % (obj.item_name)