# Generated by Django 3.0.5 on 2020-05-06 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0006_auto_20200506_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=1, max_digits=20, validators=[django.core.validators.MinValueValidator(0.1, message='Price must be above 0.1')]),
        ),
    ]
