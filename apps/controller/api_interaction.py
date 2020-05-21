import requests
import urllib.parse
from settings import *


# url = "https://fr.openfoodfacts.org/api/v0"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.json())


class OFFInteractions:
    """ Class for manages all interactions with OpenFoodFacts """

    def __init__(self):
        self.category = 'snacks'
        self.category_list = CATEGORIES

    def get_search_url(self, category, page_size, page):
        """ Method for creates the products url """

        suffixe_url_element = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category,
            'page_size': page_size,
            'page': page,
            'json': 'true'
        }
        prefixe_url = 'https://fr.openfoodfacts.org/cgi/search.pl?'

        return prefixe_url + urllib.parse.urlencode(suffixe_url_element)

    def get_product(self):
        """ Method to gets the json linked to a specific page """

        url = self.get_search_url(self.category, '2', '1')

        request = requests.get(url)

        return request.json()

    def get_product_info(self):
        """ Method to gets product essential information """

        raw_list = self.get_product()

        for product_info in raw_list['products']:
            print('Boisson:', product_info['product_name_fr'],
                  '\nNom générique:', product_info['generic_name_fr'],
                  '\nGrade nutritionnelle:', product_info['nutrition_grades_tags'][0],
                  '\nCode-barre:', product_info['code'],
                  '\nMagasin:', product_info['stores'],
                  '\nLien:', product_info['url'],
                  '\n')
