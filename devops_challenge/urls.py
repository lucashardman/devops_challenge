from django.contrib import admin
from django.urls import path
from produtos.views import produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', produtos),
]
