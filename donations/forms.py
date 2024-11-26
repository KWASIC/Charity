from django import forms
from .models import Donation, Subscriber

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'donor_name', 'donor_email', 'message', 'anonymous']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'donor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'donor_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'anonymous': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
