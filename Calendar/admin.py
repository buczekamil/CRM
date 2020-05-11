from django.contrib import admin

# Register your models here.
from Calendar.models import Event
from Clients.models import Category, TextBox, Order

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(TextBox)
admin.site.register(Order)




