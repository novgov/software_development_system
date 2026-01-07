from controller.base_controller import Controller
from model.product_model import ProductModel
from view.console_view import ConsoleView


if __name__ == "__main__":
    model = ProductModel()
    view = ConsoleView()
    controller = Controller(model, view)
    controller.show_items()
    controller.show_item_information("Кефир")
    controller.show_item_information("Продукт_0")
