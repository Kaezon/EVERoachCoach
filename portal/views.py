from django.conf import settings
from django.shortcuts import render

def dashboard(request):
    return render(request, 'public/dashboard.html', {'service_name': settings.SERVICE_NAME})