from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    store_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    store_name = models.CharField(null=False, blank=False, max_length=150, unique=True)
    store_code = models.CharField(null=False, blank=False, max_length=150, unique=True)

    def __str__(self) -> str:
        return self.store_code + " - " + self.store_name

class StoreSection(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False, blank=False)
    section_name = models.CharField(null=False, blank=False, max_length=50)
    section_number = models.IntegerField(null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return self.store.store_name + "-" + self.section_name + "#" + str(self.section_number)