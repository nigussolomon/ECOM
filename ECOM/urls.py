"""ECOM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ecom_base import urls as ecom_base_urls
from ecom_store import urls as ecom_store_urls
from ecom_sales import urls as ecom_sales_urls
from ecom_base.views import RegisterUserAPIView
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("site-admin/", admin.site.urls),
    path("api-auth", include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/',RegisterUserAPIView.as_view()),
    path("base-api/", include(ecom_base_urls)),
    path("store-api/", include(ecom_store_urls)),
    path("sales-api/", include(ecom_sales_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

