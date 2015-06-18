__author__ = 'Luke Merrett'

from cmdline.cmdlineparser import CmdLineParser
from evernoteclient.operations import EvernoteOperations

if __name__ == "__main__":
    parser = CmdLineParser()
    operations = EvernoteOperations()

    args = parser.parse_args()

    if args.list_notebooks:
        operations.print_list_of_notebooks()

    if args.create_note:
        operations.create_new_note(args.create_note[0], args.create_note[1])