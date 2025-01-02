from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Service, Order

def home(request):
    return render(request, 'home.html')

def vehicles_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles_list.html', {'vehicles': vehicles})

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services_list.html', {'services': services})

def driver_schedule(request):
    if request.user.is_authenticated and hasattr(request.user, 'driver'):
        orders = Order.objects.filter(driver=request.user.driver)
        return render(request, 'driver_schedule.html', {'orders': orders})
    else:
        return HttpResponse("Unauthorized", status=401)