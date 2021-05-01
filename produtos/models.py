from datetime import datetime

from django.db import models


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, null=False)
    sku = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=1024)
    price = models.FloatField(null=False)
    created = models.DateTimeField(default=datetime.now, blank=True, null=False)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class ProductBarcode(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self):
        return self.barcode


class ProductAttribute(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, null=False)
    value = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name