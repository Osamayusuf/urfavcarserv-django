from django import forms
from .models import Booking, Contact

SERVICE_CHOICES = [
    ('', 'Select A Service'),
    ('Diagnostic Test', 'Diagnostic Test'),
    ('Engine Servicing', 'Engine Servicing'),
    ('Tires Replacement', 'Tires Replacement'),
    ('Oil Changing', 'Oil Changing'),
    ('Brake Service', 'Brake Service'),
    ('Electrical Repairs', 'Electrical Repairs'),
    ('AC Service', 'AC Service'),
    ('Vacuum Cleaning', 'Vacuum Cleaning'),
]

TIME_CHOICES = [
    ('', 'Preferred Time'),
    ('07:00 AM - 09:00 AM', '07:00 AM - 09:00 AM'),
    ('09:00 AM - 11:00 AM', '09:00 AM - 11:00 AM'),
    ('11:00 AM - 01:00 PM', '11:00 AM - 01:00 PM'),
    ('02:00 PM - 04:00 PM', '02:00 PM - 04:00 PM'),
    ('04:00 PM - 06:00 PM', '04:00 PM - 06:00 PM'),
]

class BookingForm(forms.ModelForm):
    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'service', 'date', 'time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Special Request or Vehicle Details'
            }),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mt-1 form-input',
                'placeholder': 'John Doe'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mt-1 form-input',
                'placeholder': 'john@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control mt-1 form-input',
                'placeholder': '+254 ...'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control mt-1 form-input',
                'placeholder': 'How can we help?'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control mt-1',
                'rows': 5,
                'placeholder': 'Write your message here...'
            }),
        }