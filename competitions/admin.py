from django.contrib import admin
from .models import Delivery, Product, TicketOrder


admin.site.register(Delivery)
admin.site.register(Product)
admin.site.register(TicketOrder)

