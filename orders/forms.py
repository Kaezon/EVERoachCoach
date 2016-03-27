from django.forms import ModelForm, ModelChoiceField
import models
from django.forms.models import inlineformset_factory
from stock.models import StockItem
from .models import *

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('order_price',)
    def __init__(self, *args, **kwargs):
        super(AddOrderForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = StockItem.objects.all()
        self.fields['item'].label_from_instance = lambda obj: "%s" % (obj.item_name)