__author__ = 'Luke Merrett'

import settings
from evernoteclient.operations import EvernoteOperations

if __name__=="__main__":
    operations = EvernoteOperations()

    operations.print_list_of_notebooks()