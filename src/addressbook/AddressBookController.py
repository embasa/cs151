__author__ = 'bruno'
from addressbook.AddressBook import *
from addressbook.AddressBookDialogue import *
from addressbook.AddressBookEntryDialogue import *
from addressbook.Storage import *

class AddressBookController(object):
    """
    This class is intended to control the workflow of the project.
    It holds a reference to an instance of the current AddressBook,
    and a reference to each of the required dialogue boxes that are
    needed. Also controls access to Storage
    """
    def __init__(self):
        """
        Constructor instantiates all necessary classes objects
        :return:
        """
        self.__addressBook__ = AddressBook()
        self.__addBookDialogue__ = AddressBookDialogue()
        self.__addBookEntryDialogue__ = AddressBookEntryDialogue()

    def open(self,nameOfAddressBook):
        """
        This method uses the Storage class to populate the current
        AddressBook instance with the data corresponding of the specified
        address book
        :param nameOfAddressBook: a string of the name of the AddressBook
        :return:
        """
        print("open")

    def save(self):
        """
        This method overrides current AddressBook with the modified version
        of the AddressBook.
        :return:
        """
        print("save")

    def add(self):
        """
        This method calls the AddressbookEntryDialogue's routine as to allow it
        to add an entry to the corresponding
        :return:
        """
        print("add")

    def new(self):
        """
        This method is called to create a new AddressBook. Initially empty, so only
        the name is required.
        :return:
        """
        print("new")

    def saveAs(self,filepath):
        """
        This method calls the writeToDisk() method of the Storage class with filepath
        and with a reference to the current AddressBook
        :param filepath: a string with the filepath to save the current AddressBook
        :return:
        """
        print("saveAs")

    def print(self):
        """
        This method gives the current AddressBook to the AddressBookEntry so as to
        populate the window with the given AddressBook
        :return:
        """
        print("print")

    def quit(self):
        """
        This method closes application. Probably has a routine to do so safely
        :return:
        """
        print("quit")
