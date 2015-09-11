__author__ = 'bruno'

from addressbook.AddressBook import *
from addressbook.AddressBookDialogue import *
from addressbook.AddressBookImportDialogue import *
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
        When address book project is open there is no initial addressbook
        thus current file is empty
        :return:
        """
        self.__addressBook__ = AddressBook()
        self.__fileName__ = ""
        self.__currentDialogue__ = AddressBookDialogue()# AddressBookController always starts with this dialogue

    def new(self,addressBookName, fileName):
        """
        This method is called to create a new AddressBook. Initially empty, so only
        the name is required. Closes current AddressBook. This method doesn't have
        parameters because it will have to
        :param addressBookName: string containing name of new AddressBook
        :param fileName: string containing filepath of new AddressBook
        :return:
        """
        print("new")

    def open(self, nameOfAddressBook, fileName):
        """
        This method is used to close current AddressBook and open one with the specified
        name by passing readFromDisk() in Storage class
        :param nameOfAddressBook: a string of the name of the AddressBook
        :param fileName: fileName of AddressBook to open
        :return:
        """
        print("open")

    def close(self):
        """
        This method is used to close current AddressBook
        :return:
        """

    def save(self):
        """
        This method overrides current AddressBook with the modified version
        of the AddressBook in storage
        :return:
        """
        print("save")

    def saveAs(self, fileName):
        """
        This method calls the writeToDisk() method of the Storage class with filepath
        and with a reference to the current AddressBook
        :param fileName: a string with the filepath to save the current AddressBook
        :return:
        """
        print("saveAs")

    def quit(self):
        """
        This method closes application. Probably has a routine to do so safely
        :return:
        """
        print("quit")


    def add(self):
        """
        This method calls the AddressbookEntryDialogue's routine as to allow it
        to add an entry then it will append it to the current AddressBOok
        :return:
        """
        print("add")

    def edit(self, index):
        """
        This method is used to edit a specific entry from the current AddressBook
        with the specified index given from the dialogue
        :param index: index of element to delete
        :return:
        """
        print("edit")

    def delete(self, index):
        """
        this method gives the current AddressBook the index of the entry to delete
        :param index : index of element to delete
        :return:
        """

    def sortByLastName(self):
        """
        This method tells current AddressBook to sort by lastName
        :return:
        """
        self.__addressBook__.sortByName()

    def sortByZipCode(self):
        """
        This method tells current AddressBook to sort by zipcode
        :return:
        """
        self.__addressBook__.sortByName()

    def print(self):
        """
        This method is used to print all AddressBookEntries in 'mailing label' format
        :return:
        """
        print("print")

    def importCSV(self,mapping, fileName):
        """
        This method uses the AddressBookImportDialogue to get mapping and filepath
        of CSV file to pass information to Storage to get an array
        of AddressBookEntries to pass to the current AddressBook to append
        :param mapping: mapping for the column to fields
        :param fileName: a string locating where to import CSV file from
        :return:
        """
        print("importCSV")

    def exportCSV(self,fileName):
        """
        This method gets an array of AddressBookEntries from the current AddressBook
        to Storage to save to disk as CSV file.. Possibly saves the entire AddressBook
        :param fileName: for where to write CSV file
        :return:
        """
        print("exportCSV")
