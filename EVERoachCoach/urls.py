"""EVERoachCoach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from portal.views import dashboard
from stock.views import stock, editStock
from orders.views import order, paidOrder

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'orders/paid/(?P<order_id>\d+)', paidOrder, name='paidOrder'),
    url(r'^orders/', order, name='orders'),
    url(r'^stock/edit/(?P<stock_id>\d+)', editStock, name='editStock'),
    url(r'^stock/', stock, name='stock'),
    url(r'^admin/', admin.site.urls),
]