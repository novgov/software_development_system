from quest_2.model.base_model import Model
from quest_2.view.base_view import View


class Controller(object):
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        return self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name: str):
        item_info = self.model.get(item_name)
        if item_info:
            return self.view.show_item_information(
                item_type=self.model.item_type, item_name=item_name, item_info=item_info)
        else:
            return self.view.item_not_found(item_type=self.model.item_type, item_name=item_name)


