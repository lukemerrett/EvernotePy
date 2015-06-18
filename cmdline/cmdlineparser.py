__author__ = 'Luke Merrett'

import argparse

class CmdLineParser:
    __parser = None

    def __init__(self):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '-ln', '--list-notebooks',
            dest='list_notebooks',  # Result stored in a variable of this name
            action='store_true',  # Means we don't expect this flag key to come with a value
            help='Lists the current notebooks'
        )

        parser.add_argument(
             '-c', '--create-note',
            dest="create_note",
            nargs=2,
            help='Creates a new note',
            metavar=('"Title"', '"Body"')
        )

        self.__parser = parser

    def parse_args(self):
        return self.__parser.parse_args()
