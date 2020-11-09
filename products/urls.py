from django.urls import path
from .views import ProductsListAPIView

urlpatterns = [
    path("products/", ProductsListAPIView.as_view())
]
