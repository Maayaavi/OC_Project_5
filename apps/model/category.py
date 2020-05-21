#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion


class CategoryDatatable:
    """ This class groups all the necessary SQL request linked to the Category table """

    def create_dt(self):
        """ This method creates the category table """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS category"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = """CREATE TABLE category (
                    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    category_name VARCHAR(70) NOT NULL,
                    PRIMARY KEY (id)
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"""
                cursor.execute(sql)

    def inject_categories(self, category_list):
        """ Method to injects the categories from a list """

        with SQLconnexion() as connexion:
            for category in category_list:
                with connexion.cursor() as cursor:
                    sql = "INSERT INTO category (category_name) VALUES (%s)"
                    cursor.execute(sql, (category))
                connexion.commit()

    def get_categories_name(self):
        """ Method to gets all selected categories for the app """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                categories = []
                sql = "SELECT category_name FROM category"
                rows = cursor.execute(sql)
                for row in range(rows):
                    category = cursor.fetchone()
                    categories.append(category[0])
                return categories

    def get_categories_with_id(self):
        """ Method to gets all selected categories with thier id """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "SELECT id, category_name FROM Category"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
