# Generated by Django 3.0.5 on 2020-05-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0014_auto_20200507_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='website',
            field=models.URLField(null=True),
        ),
    ]