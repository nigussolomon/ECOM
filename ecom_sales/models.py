from django.db import models
from ecom_store.models import StoreProduct
from django.contrib.auth.models import User

CONFIRMATION_STATUSES = (
    ('pending', 'PENDING'),
    ('canceled', 'CANCELED'),
    ('delivered', 'DELIVERED'),
    ('confirmed_and_in_route', 'CONFIRMED AND IN ROUTE'),
)


class SalesOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.Case, blank=False, null=False)
    sales_order_code = models.CharField(max_length=15, blank=False, null=False)
    order_date = models.DateField(blank=False, null=False)

    def __str__(self) -> str:
        return self.sales_order_code + "-" + self.customer.username

class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, blank=False, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(StoreProduct, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    delivery_date = models.DateField()

    def __str__(self) -> str:
        return self.sales_order.sales_order_code + "-" + self.product.product_name
    
class SalesOrderConfirmation(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, blank=False, null=False)
    order_status = models.CharField(blank=False, null=False, choices=CONFIRMATION_STATUSES, max_length=30, default=CONFIRMATION_STATUSES[0])
    confirmed_delivery_date = models.DateField(blank=False, null=False)

    def __str__(self) -> str:
        return self.sales_order.sales_order_code + "-" + self.order_status

    