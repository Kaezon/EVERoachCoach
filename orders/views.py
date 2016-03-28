import requests
import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from django.forms import modelformset_factory
from .forms import *
from .models import *

def order(request):
    orders = Order.objects.filter(is_paid=False)
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order_instance = form.save(commit=False)
            stock_item = order_instance.item
            if order_instance.item_quantity < stock_item.item_count:
                order_instance.order_price = order_instance.item_quantity * stock_item.unit_cost
                stock_item.item_count -= order_instance.item_quantity
                order_instance.is_paid = False
                stock_item.save()
                form.save()
            else:
                raise Http404("You can't order more items than are in stock!")
        return HttpResponseRedirect(reverse(order))
    else:
        addOrderForm = AddOrderForm()
        return render(request, 'public/orders.html', {'addOrderForm': addOrderForm, 'orders': orders}, context_instance=RequestContext(request))

def cancelOrder(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    stock_item = order.item
    stock_item.item_count += order.item_quantity
    stock_item.save()
    order.delete()
    return HttpResponseRedirect('/orders/')
        
def paidOrder(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.is_paid = True
    order.save()
    return HttpResponseRedirect('/orders/')