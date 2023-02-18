from django.contrib import admin
from .models import SalesOrder, SalesOrderConfirmation, SalesOrderItem

admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(SalesOrderConfirmation)
