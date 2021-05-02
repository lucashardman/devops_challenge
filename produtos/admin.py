from django.contrib import admin

from produtos.models import Product, ProductAttribute, ProductBarcode


class Produtos(admin.ModelAdmin):
    list_display = ('title', 'sku', 'description', 'price', 'created', 'last_updated')
    list_display_links = ('title', 'sku')
    search_fields = ('title',)
    list_per_page = 20


class CodigoDeBarra(admin.ModelAdmin):
    list_display = ('barcode',)
    list_display_links = ('barcode',)
    search_fields = ('barcode',)
    list_per_page = 20


class Atributos(admin.ModelAdmin):
    list_display = ('name', 'value')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Product, Produtos)
admin.site.register(ProductBarcode, CodigoDeBarra)
admin.site.register(ProductAttribute, Atributos)
