from django.core.validators import MinValueValidator
from django.db import models
from phone_field import PhoneField

from Calendar.models import Event

customers_statuses = (
    (1, "Active"),
    (2, "Suspended"),
    (3, "Inactive"),
    (4, "VIP"))


class Customer(models.Model):
    customer_number = models.AutoField(primary_key=True, verbose_name='Customer ID')
    first_name = models.CharField(max_length=65, verbose_name='First name')
    last_name = models.CharField(max_length=65, verbose_name='Last name')
    phone = PhoneField()
    e_mail = models.EmailField(max_length=65, verbose_name="E-mail")
    address = models.CharField(max_length=65, verbose_name='Address')
    city = models.CharField(max_length=65, verbose_name='City')
    zip = models.CharField(max_length=6, verbose_name='Zip code')
    company = models.CharField(max_length=240, null=True, verbose_name='Company')
    status = models.IntegerField(choices=customers_statuses, default="1", verbose_name='Status')
    website = models.URLField(null=True, default="https:/")

    def __str__(self):
        return self.company


order_statuses = (
    (1, "Completed"),
    (2, "Open"),
    (3, "Suspended"),
    (4, "Canceled"),
    (5, "Closed"),

)


class Category(models.Model):
    category_name = models.TextField(max_length=20)
    category_id = models.AutoField(primary_key=True, serialize=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, serialize=True)
    product_name = models.CharField(max_length=20)
    product_price = models.FloatField(validators=[MinValueValidator(1, message='Minimum value = 10')])
    product_stock = models.IntegerField(validators=[MinValueValidator(1, message='Minimum value = 1')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


taxes = (
    (1, 0.00),
    (2, 0.05),
    (3, 0.08),
    (4, 0.23),
)

invoices_days = (
    (1, 14),
    (2, 30),
    (3, 60),

)


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Company')
    date = models.DateTimeField(auto_now_add=True)
    tax = models.IntegerField(choices=taxes)
    invoices_days = models.IntegerField(choices=invoices_days)
    status = models.IntegerField(choices=order_statuses)

    def __str__(self):
        return str(self.customer_id)


class OrderLine(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordertoline')
    product_selected = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    product_selected_name = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(1, message='Minimum quantity = 1')])
    total = models.DecimalField(max_digits=19, decimal_places=2)


class TextBox(models.Model):
    text = models.CharField(max_length=10240)

    def __str__(self):
        return self.text
