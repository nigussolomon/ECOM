from django.urls import path
from .views import SalesOrderView, SalesOrderItemView

urlpatterns = [
    path("sales_order/", SalesOrderView.as_view()),
    path("sales_order_items/", SalesOrderItemView.as_view())
]
