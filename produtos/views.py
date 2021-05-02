from rest_framework import viewsets, generics
from produtos.models import Product, ProductBarcode, ProductAttribute
from produtos.serializer import ProductSerializer, ProductBarcodeSerializer, ProductAttributeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os produtos"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductBarcodeViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os codigos de barra"""
    queryset = ProductBarcode.objects.all()
    serializer_class = ProductBarcodeSerializer


class ProductAttributeViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os atributos"""
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer





