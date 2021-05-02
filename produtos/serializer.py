from rest_framework import serializers
from produtos.models import ProductAttribute, ProductBarcode, Product


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductBarcodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductBarcode
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



