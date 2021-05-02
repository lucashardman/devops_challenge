from rest_framework import serializers
from produtos.models import ProductAttribute, ProductBarcode, Product
from produtos.validators import *


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductBarcodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductBarcode
        fields = '__all__'

    def validate(self, data):
        if not barcode_valido(data['barcode']):
            raise serializers.ValidationError('O código de barras deve conter apenas caracteres numéricos')
        return data


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if not sku_valido(data['sku']):
            raise serializers.ValidationError('O SKU deve conter apenas caracteres alfanumericos')
        return data


