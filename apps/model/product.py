#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion


# class Product:
#     """ Class to groups all the necessary SQL request linked to the Product table """
#
#     def create_product_dt(self):
#         """ This method creates the product database """
#         with SQLconnexion() as connexion:
#             with connexion.cursor() as cursor:
#                 sql = "DROP TABLE IF EXISTS product"
#                 cursor.execute(sql)
#
#             with connexion.cursor() as cursor:
#                 sql = """CREATE TABLE product (
#                     `id` INT NOT NULL AUTO_INCREMENT,
#                     `product_name` VARCHAR(225) NOT NULL,
#                     `product_code_barre` BIGINT NOT NULL,
#                     `product_description` TEXT NULL,
#                     `web_link` VARCHAR(225) NULL,
#                     `nutriscore` CHAR(1) NOT NULL,
#                     `registered_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
#                     PRIMARY KEY (`id`)
#                     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
#                 cursor.execute(sql)
#
#     def create_product_category_keys(self):
#         """ Method to creates a many to many foreign key for category and product """
#         with SQLconnexion() as connexion:
#              with connexion.cursor() as cursor:
#                  sql = "DROP TABLE IF EXISTS product_category"
#                  cursor.execute(sql)
#
#              with connexion.cursor() as cursor:
#                  sql = """CREATE TABLE product_category (
#                      `product_id` INT NOT NULL,
#                      `category_id` TINYINT UNSIGNED NOT NULL,
#                      PRIMARY KEY (`product_id`, `category_id`),
#                      INDEX fk_product_has_category_category1_idx (`category_id` ASC) VISIBLE,
#                      INDEX fk_product_has_category_product1_idx (`product_id` ASC) VISIBLE,
#                      CONSTRAINT `fk_product_has_category_product1`
#                          FOREIGN KEY (`product_id`)
#                          REFERENCES product (`id`)
#                          ON DELETE CASCADE
#                          ON UPDATE NO ACTION,
#                      CONSTRAINT `fk_product_has_category_category1`
#                          FOREIGN KEY (`category_id`)
#                          REFERENCES category (`id`)
#                          ON DELETE CASCADE
#                          ON UPDATE NO ACTION
#                      )ENGINE = InnoDB"""
#                  cursor.execute(sql)
#
#     def inject_product(self, product, category_name):
#         """ Method to inject a product in Product table """
#         with SQLconnexion() as connexion:
#             with connexion.cursor() as cursor:
#                 sql = """INSERT INTO Product
#                     (product_name, product_code_barre, product_description,
#                     web_link, nutriscore, category_id)
#                     SELECT %s, %s, %s, %s, %s, %s, id AS cat_id
#                     FROM Category WHERE category_name = %s"""
#                 cursor.execute(sql, (product['product_name_fr'], product['code'], product['generic_name_fr'], \
#                             product['stores'], product['url'], product['nutrition_grade_fr'], category_name))
#             connexion.commit()
#
#     def get_dirty_product_from_category(self, category_id):
#         """ This method selects on a random way 10 products from a category_id
#         (as input) with a nutriscore equal to 'd' or 'e'  """
#         with SQLconnexion() as connexion:
#             with connexion.cursor() as cursor:
#                 sql = """SELECT id, product_name FROM Product
#                     WHERE category_id = %s AND (
#                         nutriscore = 'd' OR nutriscore = 'e')
#                     ORDER BY RAND()
#                     LIMIT 10"""
#                 cursor.execute(sql, (category_id))
#                 result = cursor.fetchall()
#                 return result

class Product:
    """ This class groups all the necessary SQL request linked to the
    Product table """

    def create_product_dt(self):
        """ This method creates the product database """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS Product"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = """CREATE TABLE Product (
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    product_name TEXT NOT NULL,
                    product_sku BIGINT UNSIGNED NOT NULL,
                    product_description TEXT,
                    store VARCHAR(200),
                    website_link TEXT,
                    nutriscore CHAR(1) NOT NULL,
                    category_id TINYINT UNSIGNED NOT NULL,
                    PRIMARY KEY (id)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
                cursor.execute(sql)

    def create_product_category_keys(self):
        """ This method creates a foreign key on category_id data """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """ALTER TABLE Product
                    ADD CONSTRAINT fk_product_category_id
                    FOREIGN KEY (category_id)
                    REFERENCES Category (id) ON DELETE CASCADE"""
                cursor.execute(sql)

    def inject_product(self, product, category_name):
        """ This method inject a product in Product table """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """INSERT INTO Product
                    (product_name, product_sku, product_description, store,
                    website_link, nutriscore, category_id)
                    SELECT %s, %s, %s, %s, %s, %s, id AS cat_id
                    FROM Category WHERE category_name = %s"""
                cursor.execute(sql, (product['product_name_fr'], product['code'], product['generic_name_fr'], \
                            product['stores'], product['url'], product['nutrition_grade_fr'], category_name))
            connexion.commit()

    def get_product_from_ref(self, product_ref):
        """ This method gets a product from product table thanks to the product
        ref """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """SELECT id FROM Product
                    WHERE product_sku = %s"""
                cursor.execute(sql, (product_ref))
                result = cursor.fetchone()
                return result[0]

    def get_dirty_product_from_category(self, category_id):
        """ This method selects on a random way 10 products from a category_id
        (as input) with a nutriscore equal to 'd' or 'e'  """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """SELECT id, product_name FROM Product
                    WHERE category_id = %s AND (
                        nutriscore = 'd' OR nutriscore = 'e')
                    ORDER BY RAND()
                    LIMIT 10"""
                cursor.execute(sql, (category_id))
                result = cursor.fetchall()
                return result

    def get_subsitute_products(self, category_id):
        """ This method selects 5 products on a random way from a category_id
        (as input) with  nutriscore equal to 'a' """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = """SELECT product_name, product_description, store,
                    website_link, nutriscore, product_sku
                    FROM Product
                    WHERE category_id = %s AND nutriscore = 'a'
                    ORDER BY RAND()
                    LIMIT 5"""
                cursor.execute(sql, (category_id))
                result = cursor.fetchall()
                return result
