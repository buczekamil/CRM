from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=254)
    start_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    end_date = models.DateField( verbose_name='End date:  ')

# Create your models here.
