#! /usr/bin/env python3
# coding: utf-8

from apps.model.category import Category
from apps.model.product import Product
from apps.model.store import Store
from apps.view_cli.consolecreateview import ConsoleCreateView
from .dbinjection import InjectData


class CreateDatatable:
    """ Class for manages the creation of the datatable. """

    def __init__(self):
        self.db_category = Category()
        self.db_product = Product()
        self.db_store = Store()
        self.db_injection = InjectData()
        self.interface = ConsoleCreateView()

    def prepare(self):
        """ Method to creates all the necessary databases for the application """

        # Data tables are created
        self.interface.start_db_creation()
        self.db_category.create_category_dt()
        self.db_product.create_product_dt()
        self.db_store.create_store_dt()

        # Foreign keys are created
        self.db_product.create_product_category_keys()
        # self.db_store.create_product_store_keys()

        # Databases are feeded
        self.interface.start_get_categories()
        self.db_injection.feed_categories()
            # feed product
            # feed store
        self.interface.end_creation()

        # Update database if new data

