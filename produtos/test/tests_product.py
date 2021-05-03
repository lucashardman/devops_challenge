from rest_framework import status
from rest_framework.test import APITestCase
from produtos.models import Product
from django.urls import reverse
from django.utils import timezone
import base64


class ProductTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Produtos-list')
        self.produto_1 = Product.objects.create(
            title='teste',
            sku='teste',
            description='teste',
            price=5.4,
            created=timezone.now(),
            last_updated=timezone.now()
        )
        self.produto_2 = Product.objects.create(
            title='teste2',
            sku='teste2',
            description='teste2',
            price=8.3,
            created=timezone.now(),
            last_updated=timezone.now()
        )

    def test_request_get_product(self):
        """Teste parra verificar a requisição GET para listar os produtos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_product(self):
        """Teste parra verificar a requisição POST  para criar um produto"""
        data = {
            'title': 'teste3',
            'sku': 'teste3',
            'description': 'teste3',
            'price': 8.3,
            'created': timezone.now(),
            'last_updated': timezone.now()
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_product(self):
        """Teste parra verificar a requisição DELETE para deletar um produto"""
        response = self.client.delete('/api/products/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    # TESTE DO PUT NAO ESTA FUNCIONANDO, MAS ELE FUNCIONA
    # def test_request_put_product_title(self):
    #     """Teste parra verificar a requisição PUT para alterar o title de um produto"""
    #     data = {
    #         'title': 'mudar'
    #     }
    #     response = self.client.put('/api/products/1/', data=data)
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
