import sys
import os

from apps.view_cli.consoleapplicationview import ConsoleApplicationView
from apps.model.category import Category


class Menu:
    """Class for print the main menu"""

    def __init__(self):
        self.interface = ConsoleApplicationView()
        self.db_category = Category()

    def home_menu(self):
        """Method for print the main selection menu"""
        self.clean_screen()
        print("\n##############################")
        print("#  Bienvenue sur PyFoodSubs  #")
        print("##############################")
        print("")
        print(" 1. Vous souhaitez remplacer un aliment?")
        print(" 2. Retrouver vos aliments substitués.")
        print("\n")
        print("00. Quitter")
        print("\n")

    def category_selection_menu(self, category_tuple):
        """Method for print the food category selection menu"""
        self.clean_screen()

        self.cat_id_selected = 0 #to be sure to ask category each time
        self.cat_information = self.db_category.get_categories_with_id()
        self.interface.print_category_selection(self.cat_information)
        while self.cat_id_selected < 1 or self.cat_id_selected > len(self.cat_information):
            try:
                self.cat_id_selected = int(input("\nVotre sélection : "))
            except:
                self.interface.print_error_input_not_int()
        self.interface.print_category_selected(self.cat_information, self.cat_id_selected)

    def saved_menu(self):
        """Method for print all saved substituted food """
        self.clean_screen()
        print("Sélectionnez l'aliment que vous avez enregistré.")
        print(" 1. Aliment 1")
        print(" 2. Aliment 2")
        print(" 3. Aliment 3")
        print(" 4. Aliment 4")
        print(" 5. Aliment 5")

    def clean_screen(self):
        """Method for clear the screen"""
        if sys.platform.startswith("win"):
            # If OS Windows
            os.system("cls")
        else:
            # If OS Linux or UNIX
            os.system("clear")
