from django.forms import ModelForm
import models
from django.forms.models import inlineformset_factory
from stock import models

OrderFormSet = inlineformset_factory(Order, StockItem, can_delete=False)