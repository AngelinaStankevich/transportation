from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Vehicle, Service, Order, Driver
from .filters import VehicleFilter, ServiceFilter, OrderFilter
from .forms import DriverRegistrationForm, RegistrationForm
from .api_utils import get_weather


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
    vehicles = Vehicle.objects.all()
    services = Service.objects.all()
    drivers = Driver.objects.all()
    return render(request, 'shipping/public_info.html', {
        'vehicles': vehicles,
        'services': services,
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


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Автоматически авторизуем пользователя
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=orders)
    return render(request, 'orders/order_list.html', {'filter': order_filter})


@login_required
def driver_dashboard(request):
    orders = Order.objects.filter(driver=request.user.driver)
    return render(request, 'shipping/driver_dashboard.html', {'orders': orders})


@login_required
def driver_schedule(request):
    orders = Order.objects.filter(driver__user=request.user)
    filter = OrderFilter(request.GET, queryset=orders)
    return render(request, 'shipping/driver_schedule.html', {
        'filter': filter
    })


from django.shortcuts import render
from .api_utils import get_weather


def weather_info(request):
    city = request.GET.get('city', 'Moscow')  # По умолчанию Москва
    weather = get_weather(city)

    # Если погода не найдена или ошибка, то создается объект с ошибкой
    if weather.get('error'):
        weather_data = {'error': weather['error']}
    else:
        weather_data = {
            'city': weather.get('city'),
            'temperature': weather.get('temperature'),
            'description': weather.get('description'),
        }

    return render(request, 'api/weather_info.html', {'weather': weather_data})
