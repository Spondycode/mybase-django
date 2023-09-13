from django.contrib import admin
from .models import Delivery
from .models import Product
from .models import TicketOrder
from .models import CharPercent


admin.site.register(Delivery)
admin.site.register(CharPercent)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'approved', 'end_date',)
    ordering = ('owner',)
    search_fields = ('owner', 'title',)
    list_filter = ('owner', 'charity', 'end_date',)



@admin.register(TicketOrder)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'customer', 'date',)
    ordering = ('-date',)

