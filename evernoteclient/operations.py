__author__ = 'Luke Merrett'

import settings
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

class EvernoteOperations:
    __client = None

    def __init__(self):
        self.__client = EvernoteClient(token=settings.developer_token, sandbox=settings.sandbox)

    def print_list_of_notebooks(self):
        notebooks = self.get_list_of_notebooks()
        print("Found ", len(notebooks), " notebooks:")
        for notebook in notebooks:
            print("  * ", notebook.name)

    def get_list_of_notebooks(self):
        note_store = self.__client.get_note_store()
        return note_store.listNotebooks()

    def create_new_note(self, title, body, *notebook_guid):
        note_store = self.__client.get_note_store()

        note = Types.Note()
        note.title = title
        if notebook_guid:
            note.notebookGuid = notebook_guid

        self.__write_note_content(note, body)

        created_note = note_store.createNote(note)

        print('"' + title + '" note has been created')

        return created_note

    @staticmethod
    def __write_note_content(note, body):
        note.content = '<?xml version="1.0" encoding="UTF-8"?>'
        note.content += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>' + body + '</en-note>'