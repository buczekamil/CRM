# Generated by Django 3.0.5 on 2020-05-06 18:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0008_auto_20200506_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Customer', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(10, message='Minimum value = 10')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Minimum value = 1')]),
        ),
    ]
