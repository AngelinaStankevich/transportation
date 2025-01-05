from django import forms
from .models import Driver, User, Order


class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['full_name', 'age', 'license_number']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'client',
            'organization',
            'driver',
            'vehicle',
            'cargo_type',
            'service',
            'date',
            'cost',
            'status',
        ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }