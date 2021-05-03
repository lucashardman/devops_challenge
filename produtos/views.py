from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from produtos.models import Product, ProductBarcode, ProductAttribute
from produtos.serializer import ProductSerializer, ProductBarcodeSerializer, ProductAttributeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os produtos"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'product_id']
    search_fields = ['sku', 'title']

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductBarcodeViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os codigos de barra"""
    queryset = ProductBarcode.objects.all()
    serializer_class = ProductBarcodeSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['barcode', 'product_id']
    search_fields = ['barcode']

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ProductAttributeViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os atributos"""
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'product_id']
    search_fields = ['name']

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



