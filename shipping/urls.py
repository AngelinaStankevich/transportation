from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles/', views.vehicles_list, name='vehicles_list'),
    path('services/', views.services_list, name='services_list'),
    path('schedule/', views.driver_schedule, name='driver_schedule'),
    path('info/', views.public_info, name='public_info'),
    path('register-driver/', views.register_driver, name='register_driver'),
    path('orders/', views.order_list, name='order_list'),
    path('register/', views.register, name='register'),
    path('driver/', views.driver_dashboard, name='driver_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('weather/', views.weather_info, name='weather_info')
]
