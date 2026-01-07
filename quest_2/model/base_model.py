from abc import ABC
from enum import Enum


class Model(ABC):
    def __iter__(self):
        raise NotImplementedError()


    def get(self, item):
        raise NotImplementedError()

    @property
    def item_type(self):
        raise NotImplementedError()


class ItemType(str, Enum):
    PRODUCTS = "Продукты"
