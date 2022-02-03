from django import forms
from django.contrib.auth.models import User

from .models import Order


class OrderForm(forms.ModelForm):

    eventDate = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Дата проведения съемки')   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = [
            'firstName',
            'lastName',
            'eventDate',
            'typeVideo',
            'timeWork',
            'suggestions',
            'phone',
            'email'
        ]

