from django.urls import path
from .views import ProductsListCreateAPIView, ProductsRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("products/", ProductsListCreateAPIView.as_view()),
    path("products/<int:pk>/", ProductsRetrieveUpdateDestroyAPIView.as_view()),
] 
