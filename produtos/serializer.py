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

    # def validate_sku(self, sku):
    #     if len(sku) > 20:
    #         raise serializers.ValidationError("O sku deve ter 32 digitos no maximo")
    #     return sku
