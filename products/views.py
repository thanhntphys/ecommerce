from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializers
# Create your views here.


class ProductsListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers