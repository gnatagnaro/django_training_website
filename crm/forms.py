from django import forms


class OrderForm(forms.Form):
    'Данный класс создает поля, отображающие имена при вводе заявки на сайте'
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Телефон')
