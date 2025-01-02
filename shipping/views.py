from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Service, Order
from .filters import VehicleFilter, ServiceFilter

def home(request):
    return render(request, 'shipping/home.html')

def vehicles_list(request):
    # Применяем фильтрацию
    vehicle_filter = VehicleFilter(request.GET, queryset=Vehicle.objects.all())
    return render(request, 'shipping/vehicles_list.html', {'filter': vehicle_filter})

def services_list(request):
    # Применяем фильтрацию
    service_filter = ServiceFilter(request.GET, queryset=Service.objects.all())
    return render(request, 'shipping/services_list.html', {'filter': service_filter})

def driver_schedule(request):
    if request.user.is_authenticated and hasattr(request.user, 'driver'):
        orders = Order.objects.filter(driver=request.user.driver)
        return render(request, 'shipping/driver_schedule.html', {'orders': orders})
    else:
        return HttpResponse("Unauthorized", status=401)
