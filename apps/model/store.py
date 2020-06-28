#! /usr/bin/env python3
# coding: utf-8
from .dbconnexion import SQLconnexion


class Store:
    """ This class groups all the necessary SQL request linked to the Category table """

    def create_store_dt(self):
        """ This method creates the store table """
        with SQLconnexion() as connexion:
            with connexion.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS store"
                cursor.execute(sql)

            with connexion.cursor() as cursor:
                sql = """CREATE TABLE store (
                    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    name VARCHAR(70) NOT NULL,
                    PRIMARY KEY (id)
                    ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4"""
                cursor.execute(sql)

    def create_product_store_keys(self):
        """ Method to creates a many to many foreign key for store and product """
        with SQLconnexion() as connexion:
             with connexion.cursor() as cursor:
                 sql = "DROP TABLE IF EXISTS product_store"
                 cursor.execute(sql)

             with connexion.cursor() as cursor:
                 sql = """CREATE TABLE `product_store` (
                      `product_id` INT NOT NULL,
                      `store_id` TINYINT UNSIGNED NOT NULL,
                      PRIMARY KEY (`product_id`, `store_id`),
                      INDEX fk_product_has_store_store1_idx (`store_id` ASC) VISIBLE,
                      INDEX fk_product_has_store_product1_idx (`product_id` ASC) VISIBLE,
                      CONSTRAINT `fk_product_has_store_product1`
                        FOREIGN KEY (`product_id`)
                        REFERENCES product (`id`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION,
                      CONSTRAINT `fk_product_has_store_store1`
                        FOREIGN KEY (`store_id`)
                        REFERENCES store (`id`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION)
                    ENGINE = InnoDB;"""
                 cursor.execute(sql)

