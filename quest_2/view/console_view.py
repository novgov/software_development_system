from quest_2.view.base_view import View
from quest_2.model.base_model import ItemType


class ConsoleView(View):
    def show_item_list(self, item_type: ItemType, item_list: list):
        for item in item_list:
            print(f"Тип - {item_type}, информация - {item}")

    def show_item_information(self, item_type, item_name, item_info):
        print(f"Тип - {item_type}, Название - {item_name}, "
              f"цена: {item_info.get('цена')} качество: {item_info.get('качество')}")

    def item_not_found(self, item_type, item_name):
        print(f"Продукт {item_type} - {item_name} не найден!")
