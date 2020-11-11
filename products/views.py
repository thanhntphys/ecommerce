from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializers
# Create your views here.


class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


class ProductsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
