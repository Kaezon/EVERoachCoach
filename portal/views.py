from django.conf import settings
from django.shortcuts import render

def dashboard(request):
    return render(request, {'service_name': settings.SERVICE_NAME}, 'public/dashboard.html')