import django, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_challenge.settings')
django.setup()

from datetime import datetime
from faker import Faker
import random
from produtos.models import Product, ProductBarcode, ProductAttribute


def generate_products(qtd):
    fake = Faker('pt_BR')
    Faker.seed(10)

    for _ in range(qtd):
        title = fake.color_name()
        bar = fake.ean()
        sku = fake.md5(raw_output=False).upper()
        description = fake.text()
        price = random.randrange(1, 1000)
        created = datetime.now()
        last_updated = datetime.now()

        product = Product(title=title, sku=sku, description=description, price=price, created=created,
                          last_updated=last_updated)
        product.save()

        barcode = ProductBarcode(product_id=product, barcode=bar)
        barcode.save()

        attribute_name = fake.word()
        attribute_value = fake.word()

        attributes = ProductAttribute(product_id=product, name=attribute_name, value=attribute_value)
        attributes.save()


generate_products(5)
