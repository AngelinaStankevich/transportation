import django_filters
from .models import Vehicle, Service

class VehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = {
            'vehicle_type': ['exact'],
            'body_type': ['exact'],
            'capacity': ['gte', 'lte'],
        }

class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields = {
            'category': ['exact'],
            'price': ['gte', 'lte'],
        }
