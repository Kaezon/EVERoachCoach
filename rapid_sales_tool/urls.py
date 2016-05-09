from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^orders/cancel/$', cancelOrder, name='cancelOrder'),
    url(r'^orders/paid/$', paidOrder, name='paidOrder'),
    url(r'^orders/$', order, name='orders'),
    url(r'^stock/delete/$', deleteStock, name='deleteStock'),
    url(r'^stock/edit/(?P<stock_id>\d+)', editStock, name='editStock'),
    url(r'^stock/$', stock, name='stock')
]