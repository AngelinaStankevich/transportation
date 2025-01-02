from django.db import models
from django.contrib.auth.models import User

class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class BodyType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=15, unique=True)
    capacity = models.FloatField(help_text="Capacity in tons")

    def __str__(self):
        return f"{self.name} ({self.license_plate})"

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.full_name

class Client(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CargoType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    cargo_type = models.ForeignKey(CargoType, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} for {self.client.name}"
