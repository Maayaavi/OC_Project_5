#! /usr/bin/env python3
# coding: utf-8

from apps.model.category import Category
from apps.model.product import Product
from apps.view_cli.consoleinjectionview import ConsoleInjectionView
from .api_interaction import OFFInteractions


class InjectData:
    """ Class for manages all the actions linked to data injection into
    the database """

    def __init__(self):
        self.api = OFFInteractions()
        self.db_category = Category()
        self.db_product = Product()
        self.interface = ConsoleInjectionView

    def feed_categories(self):
        """ Method to injects the categories into the database """
        self.db_category.inject_categories(self.api.category_list)

    def feed_products(self):
        """ This method injects the products linked to the categories selected
        into the database """

        category_list = self.db_category.get_categories_name()

        page_size = 1000
        for category in category_list:
            self.interface.product_injection_per_category(category)
            page_number = self.api.get_product_pages_number(category, str(page_size))
            for page in range(1, page_number + 1, 1):
                data = self.api.get_product_page(category, str(page_size), str(page))
                self.__manage_products_injection(data['products'], category)

    def __manage_products_injection(self, data, category):
        for product in data:
            product_info = self.__get_product_information(product)
            if product_info['injection']:
                self.db_product.inject_product(product_info, category)

    def __get_product_information(self, product):
        """ This method cleans and get the needed product informations """

        product_info = {
            'injection' : True,
            'url' : '',
            'nutrition_grade_fr' : '',
            'product_name_fr' :'',
            'code' : '',
            'stores' : '',
            'generic_name_fr' : ''
        }

        for key in product_info:
            try:
                if str(product[key]).split():
                    product_info[key] = str(product[key])
                else:
                    raise KeyError
            except KeyError:
                product_info[key] = 'NULL'
                if key == 'nutrition_grade_fr' or key == 'product_name' or key == 'code':
                    product_info['injection'] = False

        return product_info
