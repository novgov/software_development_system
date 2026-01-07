from abc import ABC


class View(ABC):
    def show_item_list(self, item_type, item_list):
        raise NotImplementedError()

    def show_item_information(self, item_type, item_name, item_info):
        raise NotImplementedError()

    def item_not_found(self, item_type, item_name):
        raise NotImplementedError()
