from django.contrib import admin
from django.urls import path, include

from produtos.views import ProductViewSet, ProductAttributeViewSet, ProductBarcodeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='Produtos')
router.register('barcodes', ProductBarcodeViewSet, basename='Codigos')
router.register('attributes', ProductAttributeViewSet, basename='Atributos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
