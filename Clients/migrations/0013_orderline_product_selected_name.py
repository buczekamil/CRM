# Generated by Django 3.0.5 on 2020-05-06 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0012_remove_orderline_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='product_selected_name',
            field=models.CharField(default='n/a', max_length=50),
            preserve_default=False,
        ),
    ]
