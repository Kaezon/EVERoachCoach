import requests
import forms
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from django.forms import modelformset_factory
from .forms import *
from .models import *

def order(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order_instance = form.save(commit=False)
            stock_item = order_instance.item
            if order_instance.item_quantity < stock_item.item_count:
                order_instance.order_price = order_instance.item_quantity * stock_item.unit_cost
                stock_item.item_count -= order_instance.item_quantity
                stock_item.save()
                form.save()
            else:
                raise Http404("You can't order more items than are in stock!")
        return HttpResponseRedirect(reverse(order))
    else:
        addOrderForm = AddOrderForm()
        return render(request, 'public/orders.html', {'addOrderForm': addOrderForm, 'orders': orders}, context_instance=RequestContext(request))