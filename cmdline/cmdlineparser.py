__author__ = 'Luke Merrett'

import argparse

class CmdLineParser:
    __parser = None

    def __init__(self):
        parser = argparse.ArgumentParser()

        # store_true means we don't expect this flag key to come with a value
        parser.add_argument(
            '--list-notebooks', '-ln',
            dest='list_notebooks',
            action='store_true',
            help='Lists the current notebooks')

        self.__parser = parser

    def parse_args(self):
        return self.__parser.parse_args()
