from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Service, Order, Driver
from .filters import VehicleFilter, ServiceFilter, OrderFilter
from .forms import DriverRegistrationForm


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
        order_filter = OrderFilter(request.GET, queryset=orders)
        return render(request, 'shipping/driver_schedule.html', {'filter': order_filter})
    else:
        return HttpResponse("Unauthorized", status=401)


def public_info(request):
    vehicles = VehicleFilter(request.GET, queryset=Vehicle.objects.all())
    services = ServiceFilter(request.GET, queryset=Service.objects.all())
    drivers = Driver.objects.all()  # Предположим, модель Driver существует
    return render(request, 'shipping/public_info.html', {
        'vehicle_filter': vehicles,
        'service_filter': services,
        'drivers': drivers,
    })


def register_driver(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Driver registered successfully!")
    else:
        form = DriverRegistrationForm()
    return render(request, 'shipping/register_driver.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=orders)
    return render(request, 'orders/order_list.html', {'filter': order_filter})