from django.urls import path, include
from .views import StoreView, StoreSectionView, ProductCategoryView

urlpatterns = [
    path("my-store/", StoreView.as_view()),
    path("my-store/sections/", StoreSectionView.as_view()),
    path("categories/", ProductCategoryView.as_view())
    
]