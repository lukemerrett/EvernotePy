__author__ = 'Luke Merrett'

from cmdline.cmdlineparser import CmdLineParser
from evernoteclient.operations import EvernoteOperations

if __name__ == "__main__":
    parser = CmdLineParser()
    operations = EvernoteOperations()

    args = parser.parse_args()

    if args.list_notebooks:
        operations.print_list_of_notebooks()