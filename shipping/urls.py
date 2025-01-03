from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles/', views.vehicles_list, name='vehicles_list'),
    path('services/', views.services_list, name='services_list'),
    path('schedule/', views.driver_schedule, name='driver_schedule'),
    path('info/', views.public_info, name='public_info'),
    path('register-driver/', views.register_driver, name='register_driver'),

]
