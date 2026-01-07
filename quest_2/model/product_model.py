from random import randint
from model.base_model import Model, ItemType


class ProductModel(Model):
    def __init__(self):
        self.products = {}
        for i in range(5):
            self.products.update({f"Продукт_{i}": {"цена": randint(1, 5), "качество": randint(1, 10)}})

    def __iter__(self):
        for item in self.products:
            yield item

    @property
    def item_type(self):
        return ItemType.PRODUCTS

    def get(self, item: str):
        try:
            return self.products[item]
        except KeyError:
            return None

