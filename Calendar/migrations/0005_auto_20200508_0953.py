# Generated by Django 3.0.5 on 2020-05-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0004_auto_20200508_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='End date:  '),
        ),
    ]
