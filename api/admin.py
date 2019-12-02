from django.contrib import admin
from .models import Dinosaur, Order, OrderedItem

admin.site.register(Dinosaur)
admin.site.register(Order)
admin.site.register(OrderedItem)