from apps.view_cli.menu import Menu
from apps.view_cli.error import Error

from .api_interaction import OFFInteractions
from apps.model.category import CategoryDatatable


class Application:
    """Class for manages the different steps of the application"""
    def __init__(self):
        self.menu_print = Menu()
        self.error_print = Error()

        self.cat_info = CategoryDatatable()

    def main(self):
        """ Method for manages the main menu"""
        self.menu_print.home_menu()
        choice = input("Votre choix? ")
        if choice == "00":
            exit()
        elif choice == "1":
            self.category()
        elif choice == "2":
            pass
        else:
            self.error_print.touch_error()
            self.main()

    def category(self):
        """ Method for manages the category menu"""
        self.menu_print.category_selection_menu(self.cat_info.get_categories_with_id())
        choice = input("Votre choix? ")
        if choice == "00":
            exit()
        elif choice == "0":
            self.main()
        else:
            self.error_print.touch_error()
            self.category()
