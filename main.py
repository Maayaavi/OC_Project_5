#! /usr/bin/env python3
# coding: utf-8

import argparse

from apps.controller.application_cli import ApplicationCLI
from apps.controller.dbcreation import CreateDatatable
from apps.controller.dbupdate import UpdateDatatable


def parse_arguments():
    """ This function creates the needed arguments to create and updates
    the database manually """

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', help="""Action on Database. Type
    "-d create" to create and feed the database. Type "-d update" to force the update of
    the database""")
    return parser.parse_args()


def main():
    """ Main function """

    args = parse_arguments()

    if args.database == 'create':
        database = CreateDatatable()
        database.prepare()
    elif args.database == 'update':
        database = UpdateDatatable()
        database.update_database(True)

    application = ApplicationCLI()
    application.main()


if __name__ == "__main__":
    main()
