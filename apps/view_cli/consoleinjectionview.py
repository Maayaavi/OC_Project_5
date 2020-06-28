#! /usr/bin/env python3
# coding: utf-8


class ConsoleInjectionView:
    """ This class groups all the console's messages linked to database injections. """

    def product_injection_per_category(self, category):
        """ This method prints a message to indicate that the application
        injects the product of the X category """

        print("Téléchargement des produits de la catégorie {}".format(category))
        print("Veuillez patientez s'il vous plait.")
