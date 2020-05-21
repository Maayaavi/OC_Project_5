from apps.controller.api_interaction import OFFInteractions
from apps.controller.application_cli import Application
from apps.model.category import CategoryDatatable


def main():
    """ Main function """

    # startt = OFFInteractions()
    # start.get_product_info()

    app = Application()
    app.main()

    # start = CategoryDatatable()
    # start.create_dt()
    # start.inject_categories(OFFInteractions().category_list)
    # start.get_categories_name()
    # start.get_categories_with_id()


if __name__ == "__main__":
    main()
