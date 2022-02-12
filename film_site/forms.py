from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    required_css_class = 'required'

    eventDate = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Дата проведения съемки') 
    eventTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'), label='Время проведения съемки') 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = [
            'firstName',
            'lastName',
            'eventDate',
            'eventTime',
            'typeVideo',
            'timeWork',
            'suggestions',
            'phone',
            'email'
        ]
