class Product:
    def __init__(self, title, sku, description, price, created, last_updated, product_id=None):
        self.product_id = product_id
        self.title = title
        self.sku = sku
        self.description = description
        self.price = price
        self.created = created
        self.last_updated = last_updated


class Barcode:
    def __init__(self, product_id, barcode):
        self.product_id = product_id
        self.barcode = barcode


class Attribute:
    def __init__(self, product_id, name, value):
        self.product_id
        self.name
        self.value