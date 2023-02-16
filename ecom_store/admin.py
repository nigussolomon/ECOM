from django.contrib import admin
from .models import Store, StoreSection, ProductCategory, StoreProduct

admin.site.register(Store)
admin.site.register(StoreSection)
admin.site.register(ProductCategory)
admin.site.register(StoreProduct)
