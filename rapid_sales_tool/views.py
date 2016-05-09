import requests
import json
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect, render, get_object_or_404, HttpResponse
from django.forms import modelformset_factory
from .forms import *
from .models import *

def order(request):
    orders = Order.objects.filter(is_paid=False)
    for item in orders:
        item.markup_price = item.order_price + (item.order_price * Decimal(settings.MARKUP_VALUE))
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order_instance = form.save(commit=False)
            stock_item = order_instance.item
            if order_instance.item_quantity <= stock_item.item_count:
                order_instance.order_price = order_instance.item_quantity * stock_item.unit_cost
                stock_item.item_count -= order_instance.item_quantity
                order_instance.is_paid = False
                stock_item.save()
                form.save()
            else:
                return HttpResponseServerError(('You cannot order more than is available: {0} units').format(stock_item.item_count))
        return HttpResponseRedirect(reverse(order))
    else:
        addOrderForm = AddOrderForm()
        return render(request, 'rapid_sales_tool/orders.html', {'addOrderForm': addOrderForm, 'orders': orders, 'service_name': settings.SERVICE_NAME}, context_instance=RequestContext(request))

def cancelOrder(request):
    if request.method == 'POST':
        response = HttpResponse()
        order_id = request.POST['order_id']
        order = get_object_or_404(Order, pk=order_id)
        stock_item = order.item
        stock_item.item_count += order.item_quantity
        stock_item.save()
        order.delete()
        response.status_code = 200
        return response
    else:
        Http404("Why are you here?")
        
def paidOrder(request):
    if request.method == 'POST':
        response = HttpResponse()
        order_id = request.POST['order_id']
        order = get_object_or_404(Order, pk=order_id)
        order.is_paid = True
        order.save()
        response.status_code = 200
        return response
    else:
        Http404("Why are you here?")

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
        return render(request, 'rapid_sales_tool/stock.html', {'addItemForm': addItemForm, 'addStockForm': addStockForm, 'items': items, 'service_name': settings.SERVICE_NAME}, context_instance=RequestContext(request))
    
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

def deleteStock(request):
    if request.method == 'POST':
        response = HttpResponse()
        item_id = request.POST['item_id']
        stock_item = get_object_or_404(StockItem, pk=item_id)
        stock_item.delete()
        response.status_code = 200
        return response
    else:
        Http404("Why are you here?")