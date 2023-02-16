from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    store_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    store_name = models.CharField(null=False, blank=False, max_length=150, unique=True)
    store_code = models.CharField(null=False, blank=False, max_length=150, unique=True)

    def __str__(self) -> str:
        return self.store_code + " - " + self.store_name

class StoreSection(models.Model):
    section_name = models.CharField(null=False, blank=False, max_length=50)
    section_code = models.IntegerField(null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return self.store.store_name + "-" + self.section_name + "#" + str(self.section_number)

class ProductCategory(models.Model):
    store_section = models.ForeignKey(StoreSection, on_delete=models.CASCADE, null=False, blank=False)
    category_name = models.CharField(null=False, blank=False, max_length=30)

    def __str__(self) -> str:
        return self.category_name
class StoreProduct(models.Model):
    product_code = models.CharField(null=False, blank=False, max_length=50)
    product_name = models.CharField(null=False, blank=False, max_length=120)
    product_category = models.ForeignKey(ProductCategory, null=False, blank=False, on_delete=models.CASCADE)
    product_price = models.CharField(null=False, blank=False, max_length=20)

    def __str__(self) -> str:
        return self.product_code + " - " + self.product_name