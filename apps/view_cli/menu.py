import sys
import os


class Menu:
    """Class for print the main menu"""

    def __init__(self):
        pass

    def home_menu(self):
        """Method for print the main selection menu"""
        self.clean_screen()
        print("##############################")
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

        print("Sélectionnez la catégorie d'aliment.")
        print("")
        for category in category_tuple:
            print("{}. {}".format(category[0], category[1]))
        print("")
        print("0. Retour")
        print("00. Quitter")
        print("")

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
