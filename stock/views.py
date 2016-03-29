import requests
import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from .forms import *
from .models import *

def stock(request):
    items = StockItem.objects.all()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse(stock))
    else:
        addItemForm = AddItemForm()
        addStockForm = AddStockForm()
        return render(request, 'public/stock.html', {'addItemForm': addItemForm, 'addStockForm': addStockForm, 'items': items, 'service_name': settings.SERVICE_NAME}, context_instance=RequestContext(request))
    
def editStock(request, stock_id):
    stock_item = get_object_or_404(StockItem, pk=stock_id)
    item_instance = get_object_or_404(StockItem, pk=stock_id)
    if request.method == 'POST':
        form = AddStockForm(request.POST, instance=item_instance)
        if form.is_valid():
            item_count = form.instance.item_count + stock_item.item_count
            unit_cost = ((form.instance.item_count * form.instance.unit_cost) + (stock_item.item_count * stock_item.unit_cost)) / item_count
            form.instance.item_count = item_count
            form.instance.unit_cost = unit_cost
            form.save()
        return HttpResponseRedirect(reverse(stock))
    else:
        raise Http404("Stock item does not exist")