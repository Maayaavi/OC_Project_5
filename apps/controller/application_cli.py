#! /usr/bin/env python3
# coding: utf-8

import sys
import os

from apps.view_cli.menu import Menu
from apps.view_cli.error import Error

from apps.model.registered_product import RegisteredProductDatabase

from apps.view_cli.consoleapplicationview import ConsoleApplicationView

from .api_interaction import OFFInteractions
from apps.model.category import Category
from apps.model.product import Product

from .dbupdate import UpdateDatatable


class ApplicationCLI:
    """Class for manages the different steps of the application"""
    def __init__(self):
        self.interface = ConsoleApplicationView()
        self.db_category = Category()
        self.db_product = Product()
        self.db_registered_product = RegisteredProductDatabase()
        # self.update = UpdateDatatable()

        self.menu_print = Menu()
        self.error_print = Error()

        # self.cat_info = Category()
        self.cat_information = ()
        self.cat_id_selected = 0
        self.prd_tuple = ()
        self.subst_prd_tuple = ()
        self.play = True

    def main(self):
        """ This method manages the different steps of the application"""
        self.clean_screen()
        while self.play:
            choice = self.action_choice()
            if choice == 'research':
                self.category_selection()
                self.product_selection()
                self.selected_substitute_products()
                self.save_substitute_product()

    def category_selection(self):
        """ This method manages the category selection """
        self.clean_screen()
        self.cat_id_selected = 0 #to be sure to ask category each time
        self.categories = self.db_category.get_categories_with_id()
        self.interface.print_category_selection(self.categories)
        while self.cat_id_selected < 1 or self.cat_id_selected > len(self.categories):
            try:
                self.cat_id_selected = int(input("\nVotre Choix: "))
            except:
                self.interface.print_error_input_not_int()
        self.interface.print_category_selected(self.categories, self.cat_id_selected)

    def product_selection(self):
        """ This method manages the product selection """
        self.clean_screen()
        self.prd_tuple = self.db_product.get_dirty_product_from_category(self.cat_id_selected)
        self.interface.print_product_selection(self.prd_tuple)
        prd_number = self.__prd_input(self.prd_tuple)
        #prd_number - 1 because index starts from zero
        self.interface.print_product_selected(self.prd_tuple, prd_number - 1)

    def selected_substitute_products(self):
        """ This method manages the selection of substitute products """

        self.subst_prd_tuple = self.db_product.get_subsitute_products(self.cat_id_selected)
        self.interface.print_subsitute_products(self.subst_prd_tuple)

    def save_substitute_product(self):
        """ This method manages the substitute product registered feature """

        save = True
        while save:
            self.interface.print_save_product_question()
            answer = 'W'
            while answer != 'Y' and answer != 'N':
                answer = input("Votre réponse: ").upper()

            if answer == 'Y':
                self.interface.print_product_to_save_question()
                prd_number = self.__prd_input(self.subst_prd_tuple)
                self.__product_save_process(self.subst_prd_tuple[prd_number - 1][5])
            else:
                save = False
                self.interface.print_end_save_process_message()

    def action_choice(self):
        """This method manages the choice of the user between doing a research
        or seeing his saved products"""
        self.interface.print_action_choice()
        answer = 0
        while answer != 1 and answer != 2:
            try:
                answer = int(input("\nVotre choix:"))
            except:
                self.interface.print_error_input_not_int()

        if answer == 1:
            return 'research'

    def __prd_input(self, product_tuple):
        """ This method manages the product selection """
        prd_number = 0
        while prd_number < 1 or prd_number > len(product_tuple):
            try:
                prd_number = int(input("numéro de produit: "))
            except:
                self.interface.print_error_input_not_int()

        return prd_number

    def clean_screen(self):
        """Method for clear the screen"""
        if sys.platform.startswith("win"):
            # If OS Windows
            os.system("cls")
        else:
            # If OS Linux or UNIX
            os.system("clear")

    def __product_save_process(self, product_ref):
        """ This private method manages the process to save a product """
        product_to_save = self.db_registered_product.get_product_from_ref(product_ref)
        # Si le produit a déjà été enregistré
        if product_to_save:
            self.interface.print_product_already_saved()
        else:
            self.db_registered_product.inject_product(product_ref, 'disponible')
            self.interface.print_selected_product_to_save()
