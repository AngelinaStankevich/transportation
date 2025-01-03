from django import forms
from .models import Driver


class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['full_name', 'age', 'license_number']
