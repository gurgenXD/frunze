from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone', 'email')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия Имя Отчетсво', 'id': 'inputName', 'autofocus':'autofocus'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон', 'id': 'inputPhone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'id': 'inputEmail'}),
        }