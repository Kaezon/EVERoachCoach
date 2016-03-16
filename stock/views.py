import requests
import forms
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render

def stock(request):
    AddItemFormset = AddItemForm()
    if request.method == 'POST':
        formset = AddItemFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect(reverse(stock))
    else:
        formset = AddItemFormset()
    return render(request, 'public/stock.html', {'formset': formset})