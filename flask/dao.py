# from models import Product, Barcode, Attribute

SQL_ATUALIZA_PRODUTO = 'UPDATE product ' \
                       'SET title=%s, ' \
                       'sku=%s, ' \
                       'description=%s, ' \
                       'price=%s, ' \
                       'created={%s}, ' \
                       'last_updated=%s ' \
                       'where product_id=%s'
SQL_CRIA_PRODUTO = 'INSERT INTO product' \
                   '(product_id, title, sku, description, price, created, last_updated)' \
                   'values (%s, %s, %s, %s, %s, %s, %s)'


class ProductDao:
    def __init__(self, db):
        self.__db = db

    def save(self, product):
        cursor = self.__db.connection.cursor()
        if product.sku:
            cursor.execute(SQL_ATUALIZA_PRODUTO, (product.product_id,
                                                  product.title,
                                                  product.sku,
                                                  product.description,
                                                  product.price,
                                                  product.created,
                                                  product.last_updated))
        else:
            cursor.execute(SQL_CRIA_PRODUTO, (product.product_id,
                                              product.title,
                                              product.sku,
                                              product.description,
                                              product.price,
                                              product.created,
                                              product.last_updated))
            product.id = cursor.lastrowid
        self.__db.connection.commit()
        return product
