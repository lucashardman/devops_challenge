from django.contrib import admin
from django.urls import path, include

from produtos.views import ProductViewSet, ProductAttributeViewSet, ProductBarcodeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('produtos', ProductViewSet, basename='Produtos')
router.register('codigosdebarra', ProductBarcodeViewSet, basename='Codigos')
router.register('atributos', ProductAttributeViewSet, basename='Atributos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
