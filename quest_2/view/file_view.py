from view.base_view import View
from model.base_model import ItemType


class FileView(View):
    def __init__(self, filename: str):
        self.filename = filename

    def _write_to_file(self, message: str):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

    def show_item_list(self, item_type: ItemType, item_list: list):
        for item in item_list:
            self._write_to_file(f"Тип - {item_type}, информация - {item}")

    def show_item_information(self, item_type: ItemType, item_name: str, item_info: dict):
        self._write_to_file(
            f"Тип - {item_type}, Название - {item_name}, "
            f"цена: {item_info.get('цена')}, качество: {item_info.get('качество')}"
        )

    def item_not_found(self, item_type: ItemType, item_name: str):
        self._write_to_file(f"Продукт {item_type} - {item_name} не найден!")
