from django import forms
from django.forms import ModelForm

from Clients.models import Customer, taxes, invoices_days, Category, OrderLine


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=20)
    product_price = forms.FloatField()
    product_stock = forms.IntegerField()
    product_category = forms.ModelChoiceField(queryset=Category.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        product_price = cleaned_data.get('product_price')
        stock = cleaned_data.get('stock')
        if product_price <=0 or stock <= 0:
            raise forms.ValidationError('Nie podałeś wieku użytkownika!')

discounts = (
    (1, 0),
    (2, 10),
    (3, 15),
    (4, 20),
    (5, 25),
    (6, 30),
    (7, 35),
    (8, 40),
    (9, 45),
    (10, 50),
    (11, 55),
    (12, 60),
)
class OrderForm(forms.Form):
    customer_number = forms.ModelChoiceField(label='wpisz parzystą liczbę', queryset=Customer.objects.all())
    vat = forms.ChoiceField(choices=taxes)
    invoice_days = forms.ChoiceField(choices=invoices_days)
    discount = forms.ChoiceField(choices=discounts)



class OrderLineForm(ModelForm):
    class Meta:
        model = OrderLine
        fields = ['product_selected', 'quantity']