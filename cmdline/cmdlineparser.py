__author__ = 'Luke Merrett'

import argparse

class CmdLineParser:
    __parser = None

    def __init__(self):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--list-notebooks', '-ln',
            dest='list_notebooks',  # Result stored in a variable of this name
            action='store_true',  # Means we don't expect this flag key to come with a value
            help='Lists the current notebooks')

        self.__parser = parser

    def parse_args(self):
        return self.__parser.parse_args()
