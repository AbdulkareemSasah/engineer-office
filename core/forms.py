from django.forms import forms
from .models import Order,EmailList

class OrderForm(forms.Form):
    class Meta:
        object = Order
        fields = ['__all__']

class EmailListForm(forms.Form):
    class Meta:
        object = EmailList
        fields = ['__all__']