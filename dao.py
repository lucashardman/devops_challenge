from models import Product, Barcode, Attribute

class ProductDao:
    def __init__(self, db):
        self.__db = db

    def save(self, product):
        cursor = self.__db.connection.cursor()
        #######
        self.__db.connection.commit()
        return product