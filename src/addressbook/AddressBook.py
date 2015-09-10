__author__ = 'bruno'
from addressbook.AddressBookEntry import *

class AddressBook(object):
    """
    This class is intended to hold all necessary information for
    an individual addressbook that has been read from Storage.
    """
    def __init__(self):
        """
        Constructor that is populated with information from Storage
        :return:
        """
        self.__addressBookName__ = "addressBookName"
        self.__fileNameLocation__ = "fileNameLocation"
        self.__addressBookEntries__ = []

    def getFilenameLocation(self):
        """
        Returns the file path
        :return: a string with file path
        """
        return self.__fileNameLocation__

    def getAddressBookName(self):
        """
        Returns name of AddressBook instance
        :return: string with name
        """
        return self.__addressBookName__

    def getEntries(self):
        """
        :return: an array of all the entries AddressBook holds
        """
        return self.__addressBookEntries__

    def setFilenameLocation(self, fileNameLocation):
        """
        Setter method
        :param fileNameLocation: a String for file path
        :return:
        """
        self.__fileNameLocation__ = fileNameLocation

    def setAddressBookName(self, addressBookName):
        """
        :param addressBookName: a string for name of AddressBook
        :return:
        """
        self.__addressBookName__ = addressBookName

    def addEntry(self, entry):
        """
        :param entry: An instance of AddressBookEntry that is to be populated
        :return: unknown
        """
        print("addEntry()")

    def deleteEntry(self):
        """
        This method deletes an entry from the addressBook
        :return: A boolean with whether deleting was successful or not
        """
        print("deleteEntry()")

    def editEntry(self,entry):
        """
        Takes an AddressBook entry and edits it accordingly
        :param entry: the AddressBookEntry that needs to be edited
        :return: a copy of the reference of that AddressBookEntry
        """
        print("editEntry()")

    def searchEntry(self,name):
        """
        This method searches for an occurrence of the given name
        :param name: a string with lastName to search
        :return: a reference to the searched AddressBookEntry
        """
        print("searchEntry")

    def sortByName(self):
        """
        Uses the name Comparator that is to be used to sort the array
        of AddressBookEntry's
        :return:
        """
        print("sortByName()")

    def sortByZipcode(self):
        """
        Uses the zipcode Comparator that is to be used to sort the array
        of AddressBookEntry's
        :return:
        """
        print("sortByZipcode()")

    def toString(self):
        """
        Returns a string with all necessary information
        :return:
        """
        print("toString()")

    def getChange(self):
        """
        Returns a boolean
        :return: A boolean, True if a change has been made, False otherwise.
        """
        print("getChange()")

